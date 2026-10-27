## IMPLEMENTING WEB APPS WITH NODE.JS: SESSION MANAGEMENT

Luigi Libero Lucio Starace, PhD 

luigiliberolucio.starace@unina. 

https://luistar.github.io; https://www.squids.unina. 

https://docenti.unina.it/luigiliberolucio.stara 

## PREVIOUSLY, ON WEB TECHNOLOGIES

• Welearnedaboutserver-side programmin 

• Weimplementedourfirst web applicationusing Node.js 

• It ain’t much, but it’s honest work :) 

• Today, we’lladd one more interestingfeature to ourapp • Multiple users can sign up, log in, and manage their own To-do list 

• We’ll see soon enough that implementing these features requires a n concept: session tracking 

## SESSION TRACKING

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/ce019769-83c4-4c88-b606-b13e765f41de/4572d2981393ca62ca7f663c259c9708cde899eef5d699366872831111f188f2.jpg)


## HTTP IS STATELESS

• A given request, out the box, does not containinformation about previousrequests 

• How can the server know thata user previouslyperformedthe login? 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/ce019769-83c4-4c88-b606-b13e765f41de/5ee7352eaf2fcb69dd9a7c32de273e2844f6527aa16cbd4347bc5d67468c2bf4.jpg)


## SESSION TRACKING

• A crucial aspect of web developmen 

• The goal is maintainingstateful informationaboutuser interactions across multiple HTTP requests 

• Allows servers to «recognize» users and theiractions • This way, responses can be tailoredfor differentusers/situations! 

## A NAIVE APPROACH: USING COOKIES

• One way we’veseen for a server to «store» data across different requests is setting Cookies 

## • Idea:

1. Users send a requestto a dynamicpage, with usernameand passwordas parameter 

2. The dynamicpage checks whetherthe credentials are correct 

a. If theyare correct, the server sets Cookies to keep track of the interactio e.g.: Set-Cookie: auth=true;username=luigi 

b. If theyare not correct, the server shows an errorpage and does not set any cookie 

3. Dynamic pages thatrequireauthentication check for the authcookie 

a. If the cookie is set, theyshow the content 

b. If the cookie is not set, theyredirectto the login page 

## NAIVE APPROACH: OVERVIEW

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/ce019769-83c4-4c88-b606-b13e765f41de/50524440dc872e9dad405708ab453c7be8aabdc51a8e87f2ebc1a716e076cfd6.jpg)


## STORING SESSION DATA IN COOKIES

## HANDLING LOGIN REQUESTS

1. Wehave a login form with fields usr and pwd, using POST 

2. Weparse the requestbody as we did whensaving To-do items 

3. Wecheck whetherthe credentials are correct. If so: 

• Redirectto «/ 

• Set twoCookies 

• One stores the username. 

• The other’sjust a booleanvalue 

• Bothexpirein 1 hour 

```javascript
if(isAuthenticated){
    response.writeHead(302, {
    "Location": "/",
    "Set-Cookie": [
    `auth=true; max-age=${60*60 Clark},
    `username=${user.username}; max-age=${60*60 Clark},
    ]
    });
    response.end();
} 
```

## HANDLING LOGIN REQUESTS

## • If credentials are not correct, we show the login page and returna 401 errorcode.

```javascript
if(!isAuthenticated){
    let-renderedContent = pug.renderFile("./templates/login.pug", {"error": "Authentication failed. Check your credentials."});
    response.writeHead(401, {"Content-Type": "text/html"});
    response.end-renderedContent);
} 
```

## RETRIEVING SESSION INFORMATION

• Wewantto handle requests differentlydependingon whetherthe user is logged in or not. 

• E.g.: If an unauthorizedusers tries to visit /todo, we wantto serve him an error page with a 401 (Unauthorized). If logged users tries to do the same, we want themto see theirlist of To-dos. 

• To check whethera user has logged in, we needto check the Cookies in the HTTP requests. 

## RETRIEVING SESSION INFORMATION

## • Wewantsomethinglike the following example

```javascript
function checkUserAuthentication(request){
    let cookies = parseCookies(request);
    if(cookies.auth){
    return [true, cookies.username]
    } else {
    return [false, undefined];
    }
} 
```

• Unfortunately, we’reon ourownagain whenparsing cookies! 

## PARSING COOKIES

```javascript
function parseCookies(request){
    const list = {};
    const cookieHeader = request.headers?.cookie;
    if (!cookieHeader) return list;

    cookieHeader.split(`;').forEach(function(cookie) {
    let [ name, ...rest] = cookie.split('=');
    name = name?.trim();
    if (!name) return;
    const value = rest.join('=').trim();
    if (!value) return;
    list[name] = decodeURIComponent(value);
    });

    return list;
} 
```

## ACTING BASED ON SESSION STATUS

• All pages of ourapp will be affected by whetherthe user is authenticatedor not (e.g.: the navbarwill show «Welcome, User instead of «Login» whena user is authenticated) 

• Wewantthis information to be available to all the controller 

## ACTING BASED ON SESSION STATUS

## • One way to do that, wouldbe to modifythe handleRequest method

```javascript
function handleRequest(request, response){
    let [isUserAuthenticated, username] = checkUserAuthentication(request);
    let context = {
    isUserAuthenticated: isUserAuthenticated,
    username: username
    }

    switch(request.url){
    /* ... other routes ...*/
    case "/todo":
    handleTodoListRequest(request, response, context); break;
    }
} 
```

## ACTING BASED ON SESSION STATUS

```javascript
function handleTodoListRequest(request, response, context={}) {
    if(!context.isUserAuthenticated){
    handleError(request, response, 401, "Unauthorized!");
    } else {
    switch(request.method){
    case "GET":
    handleTodoListRequestGet(request, response, context); break;
    case "POST":
    handleTodoListRequestPost(request, response, context); break;
    default:
    handleError(request, response, 405, "Unsupported method");
    }
    }
} 
```

## LET’S LOOK AT THE CODE

• Live demo time 

• Wewill take a look at the new version of the To-do list web app, with session data stored in Cookies 

• Source Code is available in the Course Materialson Teams 

• You should check the code out, and tryto run(and debug) the web ap 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/ce019769-83c4-4c88-b606-b13e765f41de/e70cd3f8fb3e7317fbfefacb8eb065db87f720a23eea1dc98ad7f81bed8fd4b6.jpg)


## SERVER-STORED SESSIONS

## ISSUES WITH THE COOKIE APPROACH

• The cookie approachseems to work and is quitesimple to implemen 

• Unfortunately, it is affected by a critical issue 

## • Cookies are entirelycontrolledby clients!

• It is trivial to manipulatethem, making our authentication quiteuseless 

• A user could change the value of their«username» cookie to any other username, or theycould set a «username» cookie on theirown, withoutever visiting the login page. 

• These tampering issues can be addressed by using signed cookies 

• Server signs cookies using its private key. As long as the private key is secure, server can recognize tamperedcookies 

## MORE ISSUES WITH COOKIES

• Issues are not limited to users tampering with the cookie data 

• Browsers enforce limitationson Cookies to avoid performance issues 

• Cookie size is generallylimited to 4096 bytes 

• Each host can generallystore up to 20-50 cookies per domai 

• You can learnmore aboutyourbrowser’slimits here: http://browsercookielimits.iain.gur 

## • Whatif we needto store more session data?

## INTRODUCING SESSIONS

• So, howcan we keep track of sensitive information from previous interactions and mitigate tampering issues ? 

• How can we store more data thanCookies allow us to? 

• Wecan use the Web Sessionmechanism (RFC 6265) 

## WEB SESSIONS: BASICS

• Whenthereis a needto keep track of some information across requests, the web server creates a Session for a given client 

• A Session is a data structurestoring key-value pairs, managedand stored on the serve 

• A Session is identifiedby a uniquesession id (a.k.a. session token) 

• The session id is passed to the client (generallyas a Cookie) 

• Session data remains on the server, and client cannot mess with it 

## WEB SESSIONS: AUTHENTICATION EXAMPLE

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/ce019769-83c4-4c88-b606-b13e765f41de/8fdb5b8994809ee1233b6829f058c403ff3f7686848140f2b8a0257d5c0d77ae.jpg)


1: HTTP POST /login usr=john&pwd=pass 

## User A

2: 200 OK Set-Cookie: SID=ahs37…435 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/ce019769-83c4-4c88-b606-b13e765f41de/88b9660480324021217f429113ce23131e3b4e2652acc596693755b5eaab8130.jpg)


3: HTTP GET /todos Cookie: SID=ahs37…435 

## Application Server

## User A

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/ce019769-83c4-4c88-b606-b13e765f41de/152b293ae85da9f1b51e03f3066b2ae3366a6147f34ea4609bd37f092be0e274.jpg)


## User B

4: 200 OK and shows list of todos for john 

5: HTTP GET /todos 

6: Redirect to login page. 

## Session data

## Session id: ahs37gfw…asi3ff435

Key Key 

auth auth 

ValueValue 

usenameusename 

TrueTrue 

johnjohn 

## Session id: 4fg23g54…ssdf23g43u

Key 

Value 

auth 

True 

usename 

billy 

## IMPLEMENTING SESSIONS FROM SCRATCH

• Implementinga basic Session mechanism in Node.js from scratch is quiteeasy 

• Wecan use the built in JavaScript Mapobjects. A first Mapassociates each Session Id with a Session, which is in turn a <Key, Value> Map. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/ce019769-83c4-4c88-b606-b13e765f41de/ee71d8b6bbafab55f8d7f6c696229158b14bcaa1af2988cccbf5ddc65089d15a.jpg)


## SESSIONS FROM SCRATCH IN NODE.JS

```javascript
class Session {
    constructor(){
    this.sessionStore = new Map();
    }

    createSession(){
    let sessionId = this.generateNewSessionId();
    this.sessionStore.set(sessionId, new Map());
    return sessionId;
    }

    storeSessionData(sessionId, key, value){
    return this.getSessionById(sessionId)?.set(key, value);
    }

    /* other methods ... */
} 
```

## USING SESSIONS

## • Whena user logs in, we create a new session, store relevantdata in it, and pass the session id as a Cookie

```javascript
if(isAuthenticated){
    //create a new session for the user
    let sessionId = session.createSession();
    session.storeSessionData(sessionId, "username", user.username);
    session.storeSessionData(sessionId, "auth", true);
    response.writeHead(302, {
    "Location": "/",
    "Set-Cookie": [
    `sessionId=${sessionId}; max-age=${60*60}'
    ]
    });
    response.end();
} 
```

## USING SESSIONS

## • Whenwe needto access session data, we can

```javascript
function handleRequest(request, response){
    let userSession = session.getSessionFromRequest(request);
    let context = {
    isUserAuthenticated: userSession?.get("auth"),
    username: userSession?.get("username")
    }
    /* rest of the code */
} 
```

```javascript
getSessionFromRequest(request){
    let requestSessionId = parseCookies(request)["sessionId"];
    return this.getSessionById(requestSessionId);
} 
```

## METHODS FOR WEB SESSION TRACKING

• Using a Cookie to store the session id is the most popularapproach • Simple, broadly-supported 

• Otherapproaches exist: 

• URL Rewriting: Session id is appendedto everyURLs as a query paramete 

• Hiddenformfields: Session ids are stored as hiddenform fields. Whena user submits a form, the Session id is submittedalong with the otherdata 

## LET’S LOOK AT THE CODE

• Live demo time 

• Wewill nowtake a look at improvedversion of the To-do list web app, with properserver-stored session mechanisms 

• Source Code is available in the Course Materialson Teams 

• You should check the code out, an tryto run(and debug) the web ap 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/ce019769-83c4-4c88-b606-b13e765f41de/dbc8d28f95d8f180046a77a3db4d35fb66f4e4b28d588f186f70de380c6c2c73.jpg)


## REFERENCES

## • Introduction to Web Applications Developme

By Carles Mateu 

Freely available on archive.orgunder the GNU Free Documentation Licen Relevant parts:Section 3.11 (Session monitoring). You can ignore the examples with Java Servlet 

## • Using HTTP cookies

MDN web doc 

https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-27/ce019769-83c4-4c88-b606-b13e765f41de/a97eddf95000d467ede6153a3ed642bd0ecb2f954a4093c4341588749c854c89.jpg)
