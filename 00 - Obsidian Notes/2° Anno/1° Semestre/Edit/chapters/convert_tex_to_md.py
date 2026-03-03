#!/usr/bin/env python3
"""Convert LaTeX chapter files to Obsidian-flavored Markdown."""

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
    in_eqnarray = False
    in_tikz = False
    in_figure = False
    tikz_depth = 0
    in_itemize = 0  # nesting depth
    in_enumerate = 0
    enum_counters = []  # stack of counters for nested enumerates
    footnote_counter = 0
    footnotes = []
    in_dfn = False
    dfn_brace_depth = 0
    in_halfframedbox = False
    hfb_depth = 0
    in_generalbox = False
    gb_depth = 0
    skip_hdashrule = False
    in_tblr = False
    tblr_rows = []
    in_split = False
    in_cases = False

    def process_inline(text: str) -> str:
        """Process inline LaTeX commands to Markdown."""
        nonlocal footnote_counter, footnotes
        
        # Handle \lstinline[...]{...} and \lstinline{...}
        text = re.sub(r'\\lstinline\[.*?\]\{(.*?)\}', r'`\1`', text)
        text = re.sub(r'\\lstinline\{(.*?)\}', r'`\1`', text)
        
        # Handle \href{url}{text}
        text = re.sub(r'\\href\{(.*?)\}\{(.*?)\}', r'[\2](\1)', text)
        
        # Handle \textbf{...} - need to handle nested braces
        text = replace_command(text, r'\textbf', '**', '**')
        
        # Handle \textit{...}
        text = replace_command(text, r'\textit', '*', '*')
        
        # Handle \underline{...}
        text = replace_command(text, r'\underline', '<u>', '</u>')
        
        # Handle \emph{...}
        text = replace_command(text, r'\emph', '*', '*')
        
        # Custom commands
        text = text.replace(r'\mcC', r'\mathcal{C}')
        text = text.replace(r'\mcM', r'\mathcal{M}')
        text = text.replace(r'\mcP', r'\mathcal{P}')
        text = text.replace(r'\mcN', r'\mathbb{N}')
        text = text.replace(r'\mbN', r'\mathbb{N}')
        text = text.replace(r'\dotminus', r'\dot{-}')
        text = text.replace(r'\nin', r'\notin')
        text = text.replace(r'\documentname{}', 'Edit')
        text = text.replace(r'\documentyear', '2024/2025')
        
        # Handle \abrakets{...} → \langle ... \rangle
        text = replace_command_math(text, r'\abrakets', r'\langle ', r' \rangle')
        # Handle \cbrakets{...} → \{ ... \}
        text = replace_command_math(text, r'\cbrakets', r'\{', r'\}')
        # Handle \rbrakets{...} → [ ... ]  
        text = replace_command_math(text, r'\rbrakets', '[', ']')
        
        # Handle inline math \(...\) → $...$
        text = re.sub(r'\\\(', '$', text)
        text = re.sub(r'\\\)', '$', text)
        
        # Handle footnotes - extract and replace with [^n]
        while r'\footnote{' in text:
            fn_start = text.index(r'\footnote{')
            # Find matching brace
            depth = 0
            fn_content_start = fn_start + len(r'\footnote{')
            i = fn_content_start
            depth = 1
            while i < len(text) and depth > 0:
                if text[i] == '{':
                    depth += 1
                elif text[i] == '}':
                    depth -= 1
                i += 1
            fn_content = text[fn_content_start:i-1]
            footnote_counter += 1
            fn_processed = process_inline(fn_content)
            footnotes.append(f"[^{footnote_counter}]: {fn_processed}")
            text = text[:fn_start] + f"[^{footnote_counter}]" + text[i:]
        
        # Handle \ref{...} → (ref: ...)  
        text = re.sub(r'\\ref\{(.*?)\}', r'*(ref: \1)*', text)
        
        # Handle \label{...} → remove inline labels
        text = re.sub(r'\\label\{.*?\}', '', text)
        
        # Clean up misc LaTeX
        text = text.replace(r'\medskip', '')
        text = text.replace(r'\bigskip', '')
        text = text.replace(r'\smallskip', '')
        text = text.replace(r'\noindent', '')
        text = text.replace(r'\centering', '')
        text = text.replace(r'\pagestyle{plain}', '')
        text = re.sub(r'\\(?:vspace|hspace)\{.*?\}', '', text)
        
        # Remove \text{} wrapper in non-math context (keep content)
        # Actually \text{} is a math command, leave it
        
        return text

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

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip comments
        if stripped.startswith('%') and not in_lstlisting:
            i += 1
            continue
            
        # Remove trailing % comments (but not in lstlisting or math)
        if not in_lstlisting and not in_equation and not in_eqnarray:
            # Remove % comments but not \%
            cleaned = re.sub(r'(?<!\\)%.*$', '', line)
            line = cleaned
            stripped = line.strip()
        
        # ---- LSTLISTING ----
        if r'\begin{lstlisting}' in stripped:
            in_lstlisting = True
            md_lines.append('```ini')
            i += 1
            continue
        
        if r'\end{lstlisting}' in stripped:
            in_lstlisting = False
            md_lines.append('```')
            i += 1
            continue
        
        if in_lstlisting:
            # Clean up lstlisting inline math (*\(...\)*)
            code_line = line
            code_line = re.sub(r'\(\*\\?\(', '', code_line)
            code_line = re.sub(r'\\?\)\*\)', '', code_line)
            # Also handle (*...*) markers
            code_line = re.sub(r'\(\*', '', code_line)
            code_line = re.sub(r'\*\)', '', code_line)
            # Remove leading whitespace normalization for code blocks
            md_lines.append(code_line.rstrip())
            i += 1
            continue
        
        # ---- TIKZ / FIGURES ----
        if r'\begin{tikzpicture}' in stripped or r'\begin{figure}' in stripped:
            in_tikz = True
            tikz_depth = 1
            # Collect tikz content to create description
            i += 1
            continue
        
        if in_tikz:
            if r'\begin{tikzpicture}' in stripped or r'\begin{figure}' in stripped:
                tikz_depth += 1
            if r'\end{tikzpicture}' in stripped or r'\end{figure}' in stripped:
                tikz_depth -= 1
                if tikz_depth <= 0:
                    in_tikz = False
                    # Check if next line has caption
                    # Add placeholder
                    if r'\end{figure}' in stripped:
                        md_lines.append('> [!info] Diagramma')
                        md_lines.append('> *Diagramma non convertibile da TikZ. Consultare il file LaTeX originale.*')
                        md_lines.append('')
            elif r'\caption{' in stripped:
                caption = re.search(r'\\caption\{(.+?)\}', stripped)
                if caption:
                    cap_text = process_inline(caption.group(1))
                    md_lines.append(f'> [!info] {cap_text}')
                    md_lines.append('> *Diagramma non convertibile da TikZ. Consultare il file LaTeX originale.*')
                    md_lines.append('')
            elif r'\subfloat[' in stripped:
                subfloat = re.search(r'\\subfloat\[(.+?)\]', stripped)
                if subfloat:
                    sf_text = process_inline(subfloat.group(1))
                    md_lines.append(f'> *{sf_text}* — Consultare il file LaTeX originale.')
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
                # Convert tblr_rows to markdown table
                if tblr_rows:
                    # Process each row
                    processed_rows = []
                    for row in tblr_rows:
                        cells = [process_inline(c.strip()) for c in row.split('&')]
                        processed_rows.append('| ' + ' | '.join(cells) + ' |')
                    if processed_rows:
                        md_lines.append(processed_rows[0])
                        # Add separator
                        num_cols = processed_rows[0].count('|') - 1
                        md_lines.append('|' + '---|' * num_cols)
                        for row in processed_rows[1:]:
                            md_lines.append(row)
                    md_lines.append('')
                i += 1
                continue
            
            # Skip tblr formatting lines
            if stripped.startswith('hlines') or stripped.startswith('vlines') or \
               stripped.startswith('rows') or stripped.startswith('columns') or \
               stripped == '}' or stripped == '{':
                i += 1
                continue
            
            # Collect table rows
            row = stripped.rstrip('\\\\').strip()
            if row and not row.startswith('{'):
                tblr_rows.append(row)
            i += 1
            continue
        
        # ---- EQUATION / EQNARRAY ----
        if r'\begin{equation}' in stripped or r'\begin{equation*}' in stripped:
            in_equation = True
            md_lines.append('$$')
            i += 1
            continue
        
        if r'\end{equation}' in stripped or r'\end{equation*}' in stripped:
            in_equation = False
            md_lines.append('$$')
            md_lines.append('')
            i += 1
            continue
        
        if r'\begin{eqnarray}' in stripped or r'\begin{eqnarray*}' in stripped:
            in_eqnarray = True
            md_lines.append('$$')
            i += 1
            continue
        
        if r'\end{eqnarray}' in stripped or r'\end{eqnarray*}' in stripped:
            in_eqnarray = False
            md_lines.append('$$')
            md_lines.append('')
            i += 1
            continue
        
        if in_equation or in_eqnarray:
            eq_line = stripped
            # Remove label in equation
            eq_line = re.sub(r'\\label\{.*?\}', '', eq_line)
            # Custom commands in math
            eq_line = eq_line.replace(r'\mcC', r'\mathcal{C}')
            eq_line = eq_line.replace(r'\mcM', r'\mathcal{M}')
            eq_line = eq_line.replace(r'\mcP', r'\mathcal{P}')
            eq_line = eq_line.replace(r'\mcN', r'\mathbb{N}')
            eq_line = eq_line.replace(r'\mbN', r'\mathbb{N}')
            eq_line = eq_line.replace(r'\dotminus', r'\dot{-}')
            eq_line = eq_line.replace(r'\nin', r'\notin')
            eq_line = replace_command_math(eq_line, r'\abrakets', r'\langle ', r' \rangle')
            eq_line = replace_command_math(eq_line, r'\cbrakets', r'\{', r'\}')
            eq_line = replace_command_math(eq_line, r'\rbrakets', '[', ']')
            eq_line = replace_command_math(eq_line, r'\textit', r'\text{', '}')
            eq_line = replace_command_math(eq_line, r'\textbf', r'\textbf{', '}')
            md_lines.append('    ' + eq_line)
            i += 1
            continue
        
        # ---- ENVIRONMENTS ----
        
        # \dfn{Title}{Content...}
        dfn_match = re.match(r'\s*\\dfn\{(.+?)\}\{', stripped)
        if dfn_match:
            title = process_inline(dfn_match.group(1))
            in_dfn = True
            dfn_brace_depth = 1
            # Count remaining braces on this line
            rest = stripped[dfn_match.end():]
            for ch in rest:
                if ch == '{': dfn_brace_depth += 1
                elif ch == '}': dfn_brace_depth -= 1
            
            md_lines.append(f'> [!definition] {title}')
            rest_processed = process_inline(rest.rstrip('}').rstrip())
            if dfn_brace_depth <= 0:
                in_dfn = False
                if rest_processed.strip():
                    md_lines.append(f'> {rest_processed}')
            else:
                if rest_processed.strip():
                    md_lines.append(f'> {rest_processed}')
            md_lines.append('')
            i += 1
            continue
        
        if in_dfn:
            # Check for closing brace
            for ch in stripped:
                if ch == '{': dfn_brace_depth += 1
                elif ch == '}': dfn_brace_depth -= 1
            
            if dfn_brace_depth <= 0:
                in_dfn = False
                content = stripped.rstrip('}').strip()
                if content:
                    md_lines.append(f'> {process_inline(content)}')
                md_lines.append('')
            else:
                processed = process_inline(stripped)
                if processed.strip():
                    md_lines.append(f'> {processed}')
            i += 1
            continue
        
        # \begin{halfframedbox}{color}{Title}
        hfb_match = re.match(r'\s*\\begin\{halfframedbox\}\{.*?\}\{(.+?)\}', stripped)
        if hfb_match:
            title = process_inline(hfb_match.group(1))
            in_halfframedbox = True
            hfb_depth = 1
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
            gb_depth = 1
            md_lines.append(f'> [!example] {title}')
            i += 1
            continue
        
        if r'\end{generalbox}' in stripped:
            in_generalbox = False
            md_lines.append('')
            i += 1
            continue
        
        # Prefix for callout environments
        callout_prefix = ''
        if in_halfframedbox or in_generalbox:
            callout_prefix = '> '
        
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
            md_lines.append(f'## {title}')
            md_lines.append('')
            i += 1
            continue
        
        subsec_match = re.match(r'\s*\\subsection\{(.+?)\}', stripped)
        if subsec_match:
            title = process_inline(subsec_match.group(1))
            md_lines.append(f'{callout_prefix}### {title}')
            md_lines.append('')
            i += 1
            continue
        
        subsubsec_match = re.match(r'\s*\\subsubsection\*?\{(.+?)\}', stripped)
        if subsubsec_match:
            title = process_inline(subsubsec_match.group(1))
            md_lines.append(f'{callout_prefix}#### {title}')
            md_lines.append('')
            i += 1
            continue
        
        para_match = re.match(r'\s*\\paragraph\*?\{(.+?)\}', stripped)
        if para_match:
            title = process_inline(para_match.group(1))
            rest = stripped[para_match.end():].strip()
            rest_processed = process_inline(rest) if rest else ''
            md_lines.append(f'{callout_prefix}**{title}** {rest_processed}'.rstrip())
            md_lines.append('')
            i += 1
            continue
        
        # ---- SPECIAL COMMANDS ----
        
        # \newpage → ---
        if stripped == r'\newpage':
            md_lines.append('---')
            md_lines.append('')
            i += 1
            continue
        
        # \introduction{...}{...}
        intro_match = re.match(r'\s*\\introduction\{(.+?)\}\{', stripped)
        if intro_match:
            author = intro_match.group(1)
            # Collect content until matching brace
            content_lines = []
            rest = stripped[intro_match.end():]
            depth = 1
            for ch in rest:
                if ch == '{': depth += 1
                elif ch == '}': depth -= 1
            content_lines.append(rest.rstrip('}').strip())
            while depth > 0:
                i += 1
                if i >= len(lines): break
                for ch in lines[i].strip():
                    if ch == '{': depth += 1
                    elif ch == '}': depth -= 1
                content_lines.append(lines[i].strip().rstrip('}').strip())
            
            md_lines.append(f'*Docente: {author}*')
            md_lines.append('')
            for cl in content_lines:
                if cl:
                    md_lines.append(process_inline(cl))
            md_lines.append('')
            i += 1
            continue
        
        # Skip formatting-only lines
        if stripped in [r'\begin{center}', r'\end{center}', r'\begin{itemize}', 
                        r'\begin{enumerate}', r'\end{itemize}', r'\end{enumerate}']:
            if stripped == r'\begin{enumerate}':
                in_enumerate += 1
                enum_counters.append(0)
            elif stripped == r'\end{enumerate}':
                in_enumerate = max(0, in_enumerate - 1)
                if enum_counters:
                    enum_counters.pop()
            elif stripped == r'\begin{itemize}':
                in_itemize += 1
            elif stripped == r'\end{itemize}':
                in_itemize = max(0, in_itemize - 1)
            i += 1
            continue
        
        # Handle enumerate with [start=N]
        enum_start_match = re.match(r'\s*\\begin\{enumerate\}\[start=(\d+)\]', stripped)
        if enum_start_match:
            in_enumerate += 1
            enum_counters.append(int(enum_start_match.group(1)) - 1)
            i += 1
            continue
        
        # Skip hdashrule
        if r'\hdashrule' in stripped or r'\textcolor' in stripped and r'\hdashrule' in stripped:
            i += 1
            continue
        
        # Skip various LaTeX commands
        if any(stripped.startswith(cmd) for cmd in [r'\pagestyle', r'\begin{scope}', 
               r'\end{scope}', r'\coordinate', r'\draw', r'\node', r'\path',
               r'\begin{subfloat}', r'\end{subfloat}']):
            i += 1
            continue
        
        # ---- LIST ITEMS ----
        item_match = re.match(r'\s*\\item\s*(?:\[(.+?)\])?\s*(.*)', stripped)
        if item_match:
            item_label = item_match.group(1)
            item_content = item_match.group(2)
            
            indent = '  ' * (max(0, in_itemize + in_enumerate - 1))
            
            if in_enumerate > 0:
                if enum_counters:
                    enum_counters[-1] += 1
                    num = enum_counters[-1]
                else:
                    num = 1
                
                if item_label:
                    # Custom label like [\(\Longleftarrow\)]
                    label_processed = process_inline(item_label)
                    prefix = f'{indent}- **{label_processed}** '
                else:
                    prefix = f'{indent}{num}. '
            else:
                if item_label:
                    label_processed = process_inline(item_label)
                    prefix = f'{indent}- **{label_processed}** '
                else:
                    prefix = f'{indent}- '
            
            content = process_inline(item_content)
            md_lines.append(f'{callout_prefix}{prefix}{content}'.rstrip())
            i += 1
            continue
        
        # ---- REGULAR TEXT ----
        
        # Skip empty or whitespace-only lines
        if not stripped:
            md_lines.append(callout_prefix.rstrip() if callout_prefix else '')
            i += 1
            continue
        
        # Skip pure LaTeX structural commands
        skip_commands = [r'\begin{split}', r'\end{split}', r'\begin{cases}', 
                        r'\end{cases}', r'\label{', r'\vdots', r'\pmb{',
                        r'\begin{halfframedbox}', r'\begin{generalbox}']
        if any(stripped == cmd for cmd in skip_commands):
            i += 1
            continue
        
        # Process the line
        processed = process_inline(stripped)
        
        # Remove leftover LaTeX commands
        processed = re.sub(r'\\\\$', '  ', processed)  # Line break
        processed = re.sub(r'\\\\(?=\s)', '  \n', processed)
        processed = processed.replace(r'\;', ' ')
        processed = processed.replace(r'\,', ' ')
        processed = processed.replace(r'\!', '')
        processed = processed.replace(r'\quad', '  ')
        processed = processed.replace(r'\qquad', '    ')
        processed = processed.replace(r'\newline', '  ')
        processed = re.sub(r'\\chktex\s+\d+', '', processed)
        processed = re.sub(r'\\chkTeX\s+\d+', '', processed)
        
        if processed.strip():
            md_lines.append(f'{callout_prefix}{processed}'.rstrip())
        else:
            md_lines.append(callout_prefix.rstrip() if callout_prefix else '')
        
        i += 1
    
    # Add footnotes at the end
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
        
        print(f"Converting {tex_file} → {md_filename}")
        
        with open(tex_path, 'r', encoding='utf-8') as f:
            tex_content = f.read()
        
        md_content = convert_tex_to_md(tex_content)
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"  → Saved to {md_path}")
    
    print("\nDone! All files converted.")


if __name__ == '__main__':
    main()
