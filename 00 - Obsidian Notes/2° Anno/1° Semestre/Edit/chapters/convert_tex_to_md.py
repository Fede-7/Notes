#!/usr/bin/env python3
"""Convert LaTeX chapter files to Obsidian-flavored Markdown.

Handles custom commands: \\dfn, \\halfframedbox, \\generalbox,
\\abrakets, \\cbrakets, \\rbrakets, \\mcC, \\mcM, \\mcP, \\mbN,
\\dotminus, \\nin, \\abs, \\lstinline, etc.
"""

import re
import os
import sys


def convert_tex_to_md(tex_content: str) -> str:
    """Convert LaTeX content to Obsidian Markdown."""
    lines = tex_content.split('\n')
    md_lines = []

    # State tracking
    in_lstlisting = False
    in_equation = False
    in_tikz = False
    tikz_depth = 0
    in_itemize = 0
    in_enumerate = 0
    enum_counters = []
    footnote_counter = 0
    footnotes = []
    in_dfn = False
    dfn_brace_depth = 0
    in_halfframedbox = False
    in_generalbox = False
    in_tblr = False
    tblr_rows = []

    def get_callout_prefix():
        """Return '> ' if inside a callout environment, else ''."""
        if in_halfframedbox or in_generalbox or in_dfn:
            return '> '
        return ''

    def replace_command(text, cmd, prefix, suffix):
        """Replace \\cmd{content} with prefix+content+suffix, handling nested braces."""
        result = text
        while cmd + '{' in result:
            idx = result.index(cmd + '{')
            content_start = idx + len(cmd) + 1
            depth = 1
            i = content_start
            while i < len(result) and depth > 0:
                if result[i] == '{':
                    depth += 1
                elif result[i] == '}':
                    depth -= 1
                i += 1
            content = result[content_start:i-1]
            result = result[:idx] + prefix + content + suffix + result[i:]
        return result

    def replace_command_math(text, cmd, prefix, suffix):
        """Replace \\cmd{content} with prefix+content+suffix for math commands."""
        return replace_command(text, cmd, prefix, suffix)

    def expand_custom_commands(text):
        """Expand all custom LaTeX commands to standard LaTeX."""
        text = text.replace(r'\mcC', r'\mathcal{C}')
        text = text.replace(r'\mcM', r'\mathcal{M}')
        text = text.replace(r'\mcP', r'\mathcal{P}')
        text = text.replace(r'\mcN', r'\mathbb{N}')
        text = text.replace(r'\mbN', r'\mathbb{N}')
        text = text.replace(r'\dotminus', r'\dot{-}')
        text = text.replace(r'\documentname{}', 'Edit')
        text = text.replace(r'\documentname', 'Edit')
        text = text.replace(r'\documentyear', '2024/2025')

        # \nin -> \notin (word-boundary safe)
        text = re.sub(r'\\nin(?![a-zA-Z])', r'\\notin', text)

        # \abrakets{...} -> \langle ... \rangle
        text = replace_command_math(text, r'\abrakets', r'\langle ', r' \rangle')
        # \cbrakets{...} -> \{ ... \}
        text = replace_command_math(text, r'\cbrakets', r'\{', r'\}')
        # \rbrakets{...} -> [ ... ]
        text = replace_command_math(text, r'\rbrakets', '[', ']')
        # \abs{...} -> |...|
        text = replace_command_math(text, r'\abs', '|', '|')

        return text

    def process_inline(text):
        """Process inline LaTeX commands to Markdown."""
        nonlocal footnote_counter, footnotes

        # Handle \lstinline[...]{...} and \lstinline{...}
        text = re.sub(r'\\lstinline\[.*?\]\{(.*?)\}', r'`\1`', text)
        text = re.sub(r'\\lstinline\{(.*?)\}', r'`\1`', text)

        # Handle \href{url}{text}
        text = re.sub(r'\\href\{(.*?)\}\{(.*?)\}', r'[\2](\1)', text)

        # Handle \textbf{...}
        text = replace_command(text, r'\textbf', '**', '**')

        # Handle \textit{...}
        text = replace_command(text, r'\textit', '*', '*')

        # Handle \underline{...}
        text = replace_command(text, r'\underline', '<u>', '</u>')

        # Handle \emph{...}
        text = replace_command(text, r'\emph', '*', '*')

        # Handle \textcolor{color}{text} -> just the text
        while r'\textcolor{' in text:
            idx = text.index(r'\textcolor{')
            brace_start = idx + len(r'\textcolor{')
            depth = 1
            ii = brace_start
            while ii < len(text) and depth > 0:
                if text[ii] == '{':
                    depth += 1
                elif text[ii] == '}':
                    depth -= 1
                ii += 1
            if ii < len(text) and text[ii] == '{':
                content_start = ii + 1
                depth = 1
                jj = content_start
                while jj < len(text) and depth > 0:
                    if text[jj] == '{':
                        depth += 1
                    elif text[jj] == '}':
                        depth -= 1
                    jj += 1
                content = text[content_start:jj-1]
                text = text[:idx] + content + text[jj:]
            else:
                break

        # Expand custom commands
        text = expand_custom_commands(text)

        # Handle inline math \(...\) -> $...$
        text = re.sub(r'\\\(', '$', text)
        text = re.sub(r'\\\)', '$', text)

        # Handle footnotes
        while r'\footnote{' in text:
            fn_start = text.index(r'\footnote{')
            fn_content_start = fn_start + len(r'\footnote{')
            depth = 1
            ii = fn_content_start
            while ii < len(text) and depth > 0:
                if text[ii] == '{':
                    depth += 1
                elif text[ii] == '}':
                    depth -= 1
                ii += 1
            fn_content = text[fn_content_start:ii-1]
            footnote_counter += 1
            fn_processed = process_inline(fn_content)
            footnotes.append(f"[^{footnote_counter}]: {fn_processed}")
            text = text[:fn_start] + f"[^{footnote_counter}]" + text[ii:]

        # Handle \ref{...}
        text = re.sub(r'~?\\ref\{(.*?)\}', r'*(ref: \1)*', text)

        # Handle \label{...} -> remove
        text = re.sub(r'\\label\{[^}]*\}', '', text)

        # Clean up misc LaTeX
        text = text.replace(r'\medskip', '')
        text = text.replace(r'\bigskip', '')
        text = text.replace(r'\smallskip', '')
        text = text.replace(r'\noindent', '')
        text = text.replace(r'\centering', '')
        text = text.replace(r'\pagestyle{plain}', '')
        text = re.sub(r'\\(?:vspace|hspace)\{.*?\}', '', text)

        return text

    def process_equation_line(line_text):
        """Process a line inside an equation environment."""
        eq = line_text
        eq = re.sub(r'\\label\{[^}]*\}', '', eq)
        eq = expand_custom_commands(eq)
        eq = replace_command_math(eq, r'\textit', r'\mathit{', '}')
        eq = replace_command_math(eq, r'\textbf', r'\mathbf{', '}')
        return eq

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip comments
        if stripped.startswith('%') and not in_lstlisting:
            i += 1
            continue

        # Remove trailing % comments (but not in lstlisting or math)
        if not in_lstlisting and not in_equation:
            cleaned = re.sub(r'(?<!\\)%.*$', '', line)
            line = cleaned
            stripped = line.strip()

        # Get current callout prefix
        cp = get_callout_prefix()

        # ---- LSTLISTING ----
        if r'\begin{lstlisting}' in stripped:
            in_lstlisting = True
            md_lines.append(f'{cp}```ini')
            i += 1
            continue

        if r'\end{lstlisting}' in stripped:
            in_lstlisting = False
            md_lines.append(f'{cp}```')
            md_lines.append('')
            i += 1
            continue

        if in_lstlisting:
            code_line = line
            # Handle (*\(...\)*) math escapes in lstlisting
            code_line = re.sub(r'\(\*\\\((.+?)\\\)\*\)', r'\1', code_line)
            # Handle remaining (*...*) markers
            code_line = re.sub(r'\(\*(.+?)\*\)', r'\1', code_line)
            md_lines.append(f'{cp}{code_line.rstrip()}')
            i += 1
            continue

        # ---- TIKZ / FIGURES ----
        if r'\begin{tikzpicture}' in stripped or r'\begin{figure}' in stripped:
            in_tikz = True
            tikz_depth = 1
            i += 1
            continue

        if in_tikz:
            if r'\begin{tikzpicture}' in stripped or r'\begin{figure}' in stripped:
                tikz_depth += 1
            if r'\end{tikzpicture}' in stripped or r'\end{figure}' in stripped:
                tikz_depth -= 1
                if tikz_depth <= 0:
                    in_tikz = False
                    if r'\end{figure}' in stripped:
                        md_lines.append(f'{cp}> [!info] Diagramma')
                        md_lines.append(f'{cp}> *Diagramma non convertibile da TikZ. Consultare il file LaTeX originale.*')
                        md_lines.append('')
            elif r'\caption{' in stripped:
                caption = re.search(r'\\caption\{(.+?)\}', stripped)
                if caption:
                    cap_text = process_inline(caption.group(1))
                    md_lines.append(f'{cp}> [!info] {cap_text}')
                    md_lines.append(f'{cp}> *Diagramma non convertibile da TikZ. Consultare il file LaTeX originale.*')
                    md_lines.append('')
            i += 1
            continue

        # ---- TBLR TABLES ----
        if r'\begin{tblr}' in stripped:
            in_tblr = True
            tblr_rows = []
            i += 1
            continue

        if in_tblr:
            if r'\end{tblr}' in stripped:
                in_tblr = False
                if tblr_rows:
                    processed_rows = []
                    for row in tblr_rows:
                        cells = [process_inline(c.strip()) for c in row.split('&')]
                        processed_rows.append('| ' + ' | '.join(cells) + ' |')
                    if processed_rows:
                        md_lines.append(f'{cp}{processed_rows[0]}')
                        num_cols = processed_rows[0].count('|') - 1
                        md_lines.append(f'{cp}|' + '---|' * num_cols)
                        for row in processed_rows[1:]:
                            md_lines.append(f'{cp}{row}')
                    md_lines.append('')
                i += 1
                continue
            if stripped.startswith('hlines') or stripped.startswith('vlines') or \
               stripped.startswith('rows') or stripped.startswith('columns') or \
               stripped == '}' or stripped == '{':
                i += 1
                continue
            row = stripped.rstrip('\\\\').strip()
            if row and not row.startswith('{'):
                tblr_rows.append(row)
            i += 1
            continue

        # ---- EQUATION / EQNARRAY ----
        if re.match(r'\\begin\{(equation|eqnarray)\*?\}', stripped):
            in_equation = True
            md_lines.append(f'{cp}$$')
            i += 1
            continue

        if re.match(r'\\end\{(equation|eqnarray)\*?\}', stripped):
            in_equation = False
            md_lines.append(f'{cp}$$')
            md_lines.append('')
            i += 1
            continue

        if in_equation:
            eq_line = process_equation_line(stripped)
            eq_stripped = eq_line.strip()
            # Keep begin/end cases for KaTeX, skip split/aligned wrappers
            if re.match(r'\\(begin|end)\{(split|aligned)\}', eq_stripped):
                i += 1
                continue
            if re.match(r'\\(begin|end)\{cases\}', eq_stripped):
                md_lines.append(f'{cp}    {eq_stripped}')
                i += 1
                continue
            md_lines.append(f'{cp}    {eq_line}')
            i += 1
            continue

        # ---- ENVIRONMENTS ----

        # \dfn{Title}{Content...}
        dfn_match = re.match(r'\s*\\dfn\{(.+?)\}\{', stripped)
        if dfn_match:
            title = process_inline(dfn_match.group(1))
            in_dfn = True
            dfn_brace_depth = 1
            rest = stripped[dfn_match.end():]
            # Count braces in rest
            for ch in rest:
                if ch == '{':
                    dfn_brace_depth += 1
                elif ch == '}':
                    dfn_brace_depth -= 1

            md_lines.append(f'> [!definition] {title}')

            if dfn_brace_depth <= 0:
                in_dfn = False
                # Remove the closing brace of \dfn
                last_brace = rest.rfind('}')
                if last_brace >= 0:
                    rest_content = rest[:last_brace]
                else:
                    rest_content = rest
                rest_processed = process_inline(rest_content.strip())
                if rest_processed.strip():
                    md_lines.append(f'> {rest_processed}')
                md_lines.append('')
            else:
                # Multi-line dfn: process rest through process_inline (keeps all braces)
                rest_processed = process_inline(rest.strip())
                if rest_processed.strip():
                    md_lines.append(f'> {rest_processed}')
            i += 1
            continue

        if in_dfn:
            # Count braces BEFORE processing
            for ch in stripped:
                if ch == '{':
                    dfn_brace_depth += 1
                elif ch == '}':
                    dfn_brace_depth -= 1

            if dfn_brace_depth <= 0:
                in_dfn = False
                # Remove the closing brace of \dfn
                last_brace = stripped.rfind('}')
                if last_brace >= 0:
                    content = stripped[:last_brace]
                else:
                    content = stripped
                content = content.strip()
                if content:
                    md_lines.append(f'> {process_inline(content)}')
                md_lines.append('')
            else:
                # Check for equation environments inside dfn
                if re.match(r'\\begin\{(equation|eqnarray)\*?\}', stripped):
                    in_equation = True
                    md_lines.append('> $$')
                    i += 1
                    continue
                if re.match(r'\\end\{(equation|eqnarray)\*?\}', stripped):
                    in_equation = False
                    md_lines.append('> $$')
                    md_lines.append('')
                    i += 1
                    continue
                # Check for lstlisting inside dfn
                if r'\begin{lstlisting}' in stripped:
                    in_lstlisting = True
                    md_lines.append('> ```ini')
                    i += 1
                    continue
                if r'\end{lstlisting}' in stripped:
                    in_lstlisting = False
                    md_lines.append('> ```')
                    md_lines.append('')
                    i += 1
                    continue
                # Check for list environments inside dfn
                if stripped == r'\begin{itemize}':
                    in_itemize += 1
                    i += 1
                    continue
                if stripped == r'\end{itemize}':
                    in_itemize = max(0, in_itemize - 1)
                    i += 1
                    continue
                if stripped == r'\begin{enumerate}' or re.match(r'^\\begin\{enumerate\}$', stripped):
                    in_enumerate += 1
                    enum_counters.append(0)
                    i += 1
                    continue
                if stripped == r'\end{enumerate}':
                    in_enumerate = max(0, in_enumerate - 1)
                    if enum_counters:
                        enum_counters.pop()
                    i += 1
                    continue
                # Check for \item inside dfn
                item_match = re.match(r'\s*\\item\s*(?:\[(.+?)\])?\s*(.*)', stripped)
                if item_match:
                    item_label = item_match.group(1)
                    item_content = item_match.group(2)
                    indent = '  ' * max(0, in_itemize + in_enumerate - 1)
                    if in_enumerate > 0:
                        if enum_counters:
                            enum_counters[-1] += 1
                            num = enum_counters[-1]
                        else:
                            num = 1
                        if item_label and item_label.strip():
                            label_processed = process_inline(item_label)
                            prefix = f'{indent}- **{label_processed}** '
                        else:
                            prefix = f'{indent}{num}. '
                    else:
                        if item_label and item_label.strip():
                            label_processed = process_inline(item_label)
                            prefix = f'{indent}- **{label_processed}** '
                        else:
                            prefix = f'{indent}- '
                    content = process_inline(item_content)
                    md_lines.append(f'> {prefix}{content}'.rstrip())
                    i += 1
                    continue

                processed = process_inline(stripped)
                if processed.strip():
                    md_lines.append(f'> {processed}')
                elif not stripped:
                    md_lines.append('>')
            i += 1
            continue

        # \begin{halfframedbox}{color}{Title}
        hfb_match = re.match(r'\s*\\begin\{halfframedbox\}\{.*?\}\{(.+?)\}', stripped)
        if hfb_match:
            title = process_inline(hfb_match.group(1))
            in_halfframedbox = True
            md_lines.append(f'> [!theorem] {title}')
            i += 1
            continue

        if r'\end{halfframedbox}' in stripped:
            in_halfframedbox = False
            md_lines.append('')
            i += 1
            continue

        # \begin{generalbox}[options]{Title}
        gb_match = re.match(r'\s*\\begin\{generalbox\}(?:\[.*?\])?\{(.+?)\}', stripped)
        if gb_match:
            title = process_inline(gb_match.group(1))
            in_generalbox = True
            md_lines.append(f'> [!example] {title}')
            i += 1
            continue

        if r'\end{generalbox}' in stripped:
            in_generalbox = False
            md_lines.append('')
            i += 1
            continue

        # ---- HEADINGS ----
        ch_match = re.match(r'\s*\\chapter\{(.+?)\}', stripped)
        if ch_match:
            title = process_inline(ch_match.group(1))
            md_lines.append(f'# {title}')
            md_lines.append('')
            i += 1
            continue

        sec_match = re.match(r'\s*\\section\{(.+?)\}', stripped)
        if sec_match:
            title = process_inline(sec_match.group(1))
            md_lines.append(f'{cp}## {title}')
            md_lines.append('')
            i += 1
            continue

        subsec_match = re.match(r'\s*\\subsection\{(.+?)\}', stripped)
        if subsec_match:
            title = process_inline(subsec_match.group(1))
            md_lines.append(f'{cp}### {title}')
            md_lines.append('')
            i += 1
            continue

        subsubsec_match = re.match(r'\s*\\subsubsection\*?\{(.+?)\}', stripped)
        if subsubsec_match:
            title = process_inline(subsubsec_match.group(1))
            md_lines.append(f'{cp}#### {title}')
            md_lines.append('')
            i += 1
            continue

        para_match = re.match(r'\s*\\paragraph\*?\{(.+?)\}(.*)', stripped)
        if para_match:
            title = process_inline(para_match.group(1))
            rest = para_match.group(2).strip() if para_match.group(2) else ''
            rest_processed = process_inline(rest) if rest else ''
            md_lines.append(f'{cp}**{title}** {rest_processed}'.rstrip())
            md_lines.append('')
            i += 1
            continue

        # ---- SPECIAL COMMANDS ----

        # \newpage
        if stripped == r'\newpage':
            md_lines.append('---')
            md_lines.append('')
            i += 1
            continue

        # \introduction{...}{...}
        intro_match = re.match(r'\s*\\introduction\{(.+?)\}\{', stripped)
        if intro_match:
            author = intro_match.group(1)
            content_lines_buf = []
            rest = stripped[intro_match.end():]
            depth = 1
            for ch in rest:
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
            content_lines_buf.append(rest.rstrip('}').strip())
            while depth > 0:
                i += 1
                if i >= len(lines):
                    break
                for ch in lines[i].strip():
                    if ch == '{':
                        depth += 1
                    elif ch == '}':
                        depth -= 1
                content_lines_buf.append(lines[i].strip().rstrip('}').strip())
            md_lines.append(f'*Docente: {author}*')
            md_lines.append('')
            for cl in content_lines_buf:
                if cl:
                    md_lines.append(process_inline(cl))
            md_lines.append('')
            i += 1
            continue

        # Skip/handle list environments
        if stripped in [r'\begin{center}', r'\end{center}']:
            i += 1
            continue

        if stripped == r'\begin{itemize}' or re.match(r'^\\begin\{itemize\}$', stripped):
            in_itemize += 1
            i += 1
            continue

        if stripped == r'\end{itemize}':
            in_itemize = max(0, in_itemize - 1)
            i += 1
            continue

        if stripped == r'\begin{enumerate}' or re.match(r'^\\begin\{enumerate\}$', stripped):
            in_enumerate += 1
            enum_counters.append(0)
            i += 1
            continue

        enum_start_match = re.match(r'\s*\\begin\{enumerate\}\[start=(\d+)\]', stripped)
        if enum_start_match:
            in_enumerate += 1
            enum_counters.append(int(enum_start_match.group(1)) - 1)
            i += 1
            continue

        if stripped == r'\end{enumerate}':
            in_enumerate = max(0, in_enumerate - 1)
            if enum_counters:
                enum_counters.pop()
            i += 1
            continue

        # Skip standalone \label{} lines
        if re.match(r'^\\label\{[^}]*\}\s*$', stripped):
            i += 1
            continue

        # Skip hdashrule lines
        if r'\hdashrule' in stripped:
            i += 1
            continue

        # Skip various LaTeX formatting commands
        if any(stripped.startswith(cmd) for cmd in [
            r'\pagestyle', r'\begin{scope}', r'\end{scope}',
            r'\coordinate', r'\draw', r'\node', r'\path',
            r'\begin{subfloat}', r'\end{subfloat}'
        ]):
            i += 1
            continue

        # ---- LIST ITEMS ----
        item_match = re.match(r'\s*\\item\s*(?:\[(.+?)\])?\s*(.*)', stripped)
        if item_match:
            item_label = item_match.group(1)
            item_content = item_match.group(2)
            indent = '  ' * max(0, in_itemize + in_enumerate - 1)
            if in_enumerate > 0:
                if enum_counters:
                    enum_counters[-1] += 1
                    num = enum_counters[-1]
                else:
                    num = 1
                if item_label and item_label.strip():
                    label_processed = process_inline(item_label)
                    prefix = f'{indent}- **{label_processed}** '
                else:
                    prefix = f'{indent}{num}. '
            else:
                if item_label and item_label.strip():
                    label_processed = process_inline(item_label)
                    prefix = f'{indent}- **{label_processed}** '
                else:
                    prefix = f'{indent}- '
            content = process_inline(item_content)
            md_lines.append(f'{cp}{prefix}{content}'.rstrip())
            i += 1
            continue

        # ---- REGULAR TEXT ----

        # Skip empty lines
        if not stripped:
            md_lines.append(cp.rstrip() if cp else '')
            i += 1
            continue

        # Process the line
        processed = process_inline(stripped)

        # Remove leftover LaTeX commands
        processed = re.sub(r'\\\\$', '  ', processed)
        processed = re.sub(r'\\\\(?=\s)', '  \n', processed)
        processed = processed.replace(r'\;', ' ')
        processed = processed.replace(r'\,', ' ')
        processed = processed.replace(r'\!', '')
        processed = processed.replace(r'\quad', '  ')
        processed = processed.replace(r'\qquad', '    ')
        processed = processed.replace(r'\newline', '  ')
        processed = re.sub(r'\\chk[tT]ex\s+\d+', '', processed)

        if processed.strip():
            md_lines.append(f'{cp}{processed}'.rstrip())
        else:
            md_lines.append(cp.rstrip() if cp else '')

        i += 1

    # Build result
    result = '\n'.join(md_lines)

    # Clean up multiple blank lines
    result = re.sub(r'\n{4,}', '\n\n\n', result)

    # Add footnotes
    if footnotes:
        result += '\n\n---\n\n'
        result += '\n'.join(footnotes)

    return result


def main():
    chapters_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(chapters_dir)

    tex_files = sorted([f for f in os.listdir(chapters_dir) if f.endswith('.tex')])

    for tex_file in tex_files:
        tex_path = os.path.join(chapters_dir, tex_file)
        md_filename = tex_file.replace('.tex', '.md')
        md_path = os.path.join(parent_dir, md_filename)

        print(f"Converting {tex_file} -> {md_filename}")

        with open(tex_path, 'r', encoding='utf-8') as f:
            tex_content = f.read()

        md_content = convert_tex_to_md(tex_content)

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"  -> Saved to {md_path}")

    print("\nDone! All files converted.")


if __name__ == '__main__':
    main()
