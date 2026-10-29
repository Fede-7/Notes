## WEB FRAMEWORKS: EXPRESS

Luigi Libero Lucio Starace, PhD 

luigiliberolucio.starace@unina. 

https://docenti.unina.it/luigiliberolucio.stara 

https://luistar.github.io; https://squids.unina.i 

## PREVIOUSLY, ON WEB TECHNOLOGIES

Wedevelopeda few web apps using server-side programming 

• WeimplementedourTo-do list app using CGI and Bash ( ) 

• WeimplementedourTo-do list app using PHP 8.2 

• WeimplementedourTo-do list app using Node.js 

## Therewerea few pain points

• Lots of tediousstuff (e.g.: parse cookies, read and parse requestbodies, …) 

• No out-of-the-box session management (except for PHP) 

• No out-of-the-box middleware support (e.g.: authentication 

• No out-of-the-box templatin 

## COMMON TASKS IN WEB DEVELOPMENT

• ManagingRouting 

• Rendering template 

• ManagingWeb Sessions 

• ManagingAuthentication/Authorization 

Wedo not wantto re-inventthe wheelin everyproject, right? 

## WEB FRAMEWORKS

• A frameworkis a pre-definedset of software components, tools, and best practices thatserve as a foundationfor developingsoftware 

• Web frameworksare specifically designed to simplify and streamline the developmentof web applications 

• They provide a (structured) way to build and organize web applicatio reducing the need for developers to start from scratch and re-invent th wheel 

• Frameworks and Software Libraries are different thing 

## SOFTWARE LIBRARY

Essentially a set of functions we can call to get some job done 

• Each call does some work and thenreturnscontrol to the caller 

User code (e.g.: our main method) is in control of the executionflow 

## FRAMEWORK

• Embodysome abstract design, with more behaviourbuilt-in 

• User-written code can b plugged-in into the framewor 

• The framework is in control o the execution flow and calls use code when appropriat 

## INVERSION OF CONTROL (IoC) PRINCIPLE

• IoC is a defining feature of framework 

• The control flow is inversed from traditional imperative programmi • The responsibility of managing the control flow is shifted from the developer a framework 

• A.k.a. Hollywood’s Law: “Don't call us, we'll call you”. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/8ba020a4df23b4ac9b4eac109e4ec327d0b8fa313d268e56b7d81e8b7f25a602.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/4248a9b5a5e6fb3ed49c2e9b0fffab8095fda414118da9a142e6621693049ade.jpg)



Luigi Libero Lucio Starace, Ph.D. - University of Naples Federico II - Web Technologies Course - Lecture 18 - Web Frameworks: Express


## KEY COMPONENTS OF WEB FRAMEWORKS

## Web frameworks typically includ

## • Core functionalities:

• Routing; Request parsing; Input validation; Cookie management; Session 

## • Template Engine:

• Helps in rendering dynamic content, separating code logic from t presentation layer 

## • ORM (Object-Relational Mapping) Mechanism

• Simplifies database interactions by allowing developers to work with objec instead of SQL queries. 

## OPINIONATED FRAMEWORKS

## • Frameworks can be more or less opinionate

• A (strongly) opinionatedframework comes wit a rigid set of pre-defined conventions, bes practices, and decisions made by th framework's creators. It enforces a specific way of doing things, andleaves less wiggle room to devs. 

• Unopinionated frameworks do not enforce specific way of doing things 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/1ffe2a200f1199f2304bc44e72957990baca9fec78816d9c76728c1abc17353c.jpg)



Keep in mind, thisframewor has reallystrong opinions…


Artwork generatedusing DALL-E 3 

## OPINIONATED FRAMEWORKS

## Pros

• Ensure higherlevels of consistency across different projects 

• Can speed up development, reducingdecision fatigue 

## Cons

• May have a steeperlearning curve 

• May not be flexible enoughfor a certainproject 

Pylons 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/dcf00821fb8956901fabdddf0f50f23dfd5742595132e5bb7626bd3d77a4e14b.jpg)


## WEB FRAMEWORKS (SERVER-SIDE)

• Manyweb frameworks to choose from (e.g.: see Wikipedia) 

Falinks 


One of the aboveis not a real framework, but a Pokemon. Can you tell which one?


## EXPRESS

Fast, unopinionated, minimalist web framework for Nod 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/9b953e6610b49361e48b8bbc4a1915d7646ea1004fe6dce9422b5857eff2056a.jpg)


## THE EXPRESS FRAMEWORK

• In the web technologie course, we’ll see Express as an example 

• Fast, unopinionate minimalist we framework for Node.js 

• By a good margin, th most popular Node.js backend framewor 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/dda6deaae21f5da4be46898ae003b47fd6bce24b79bbd58a8c41de92a56097f2.jpg)



State of JavaScript 2025 Report. Source here.


## HELLO EXPRESS

## @luigi ➜ D/O/T/W/2/e/express-hello-world$ npm install express

```javascript
import express from "express";
const app = express(); // creates an express application
const PORT = 3000;
app.get('/', (req, res) => {
    res.send('Hello World!')
});
app.listen(PORT); 
```

## EXPRESS: ROUTING

• Routing refers to the way the framework determineshowto handle a requestto a given endpoin 

• A routeis definedusing appropriate methodson the app object 

• Typically using statementsof the form 

```txt
app.<METHOD>(<PATH>, callback) 
```

• Where<METHOD> and <PATH> identifyan endpoint, and callback is a functionto executeto handle requests to thatendpoin 

```javascript
app.get("/hello", (req, res) => {
    res.send("Hello");
}); 
```

```javascript
app.post("/hello", (req, res) => {
    res.send("Hello Post");
}); 
```

## EXPRESS: ROUTE PATHS

Routepaths can be strings, string patterns, or full regular expressions • In case of multiple matches, the first matchedrouteapplies 

```javascript
app.get("/webtech", (req, res) => {
    res.send("Web Technologies!");
});

//matches /webtech, /wirelesstech, /wtech, /whatever-tech, etc...
app.get(/^\w.*tech$/, (req, res) => {
    res.send("Web Technologies Regex!");
}); 
```

## EXPRESS: ROUTE PARAMETERS

• Express routescan also capturenamedURL segments called parameters, declaredin the PATH by using «:paramName» 

• The capturedparametersare made available in the req.paramsobj. 

```javascript
//if a get request is made to /student/42/exams/TecWeb app.get("/student/:student_id/exams/:exam_name", (req, res) => { res.send(req.params); //{"student_id":"42","exam_name":"TecWeb"} }); 
```

## EXPRESS: MULTIPLE ROUTE HANDLERS

• It is also possible to specify multiple handlerfunctions for a route 

• These functions behavelike middleware(we’llsee soon enough!) 

• nextis a callback to the next handlerfunctionto run 

```javascript
let f1 = function(req, res, next) {console.log("f1"); next();}
let f2 = function(req, res, next) {console.log("f2"); next();}
let f3 = function(req, res, next) {console.log("f3"); next();}

app.get("/handlers", [f1, f2, f3], (req, res) => {
    res.send("Done with all handlers");
}) 
```

## EXPRESS: WORKING WITH ROUTES

• Wecan create chainableroutesusing app.route() 

• This way, the path is specified in a single location (less redundancy), and method-specific handlersare chained. 

```javascript
app.route('/book')
    .get((req, res) => {
    res.send('Get a random book')
    })
    .post((req, res) => {
    res.send('Add a book')
    })
    .delete((req, res) => {
    res.send('Delete a book')
}); 
```

## EXPRESS: MODULAR ROUTERS

• We can also create a modular router, which can be loaded as need 

```typescript
//router.js
import express from "express";

export const router = express.Router();

router.get("/echo/:value", (req, res) => {
    res.send(req.params.value);
}); 
```

```javascript
import { router as echoRouter } from "./router.js";
const app = express();
//other routes can be defined here as done earlier...
app.use("/custom", echoRouter); //load echoRouter (optionally in a certain path)
//requests to /custom/echo/:value will be handled by the router
app.listen(3000); 
```

## EXPRESS: RESPONSE METHODS

Appropriate methods on the response object (res) should be called send a response to the client, or the request will remain hangi 

<table><tr><td>Method</td><td>Description</td></tr><tr><td>res.download()</td><td>Prompt a file to be downloaded.</td></tr><tr><td>res.end()</td><td>End the response process.</td></tr><tr><td>res.json()</td><td>Send a JSON response.</td></tr><tr><td>res.jsonp()</td><td>Send a JSON response with JSONP support.</td></tr><tr><td>res.redirect()</td><td>Redirect a request.</td></tr><tr><td>res.render()</td><td>Render a view template.</td></tr><tr><td>res.send()</td><td>Send a response of various types.</td></tr><tr><td>res.sendFile()</td><td>Send a file as an octet stream.</td></tr><tr><td>res.sendStatus()</td><td>Set the response status code and send its string representation as the response body.</td></tr></table>

```javascript
const app = express();
app.set("view engine", "pug");
app.get('/template', (req, res) => {
    res.render("template");
});
app.listen(3000); 
```

```txt
Pug Template rendered in Exp1 ✗ + √ - □ ✗
localhost:3000/template 
```

## EXPRESS: RENDERING A TEMPLATE

## Rendering a Pug Template in Express

It's a straightforward process. 

## EXPRESS: RENDERING A TEMPLATE

• Moreover, data set in the res.locals object is available to all views 

• Data set in the res.locals is available to views rendering res 

```javascript
app.get("/example", (req, res) => {
    res.locals.items = [
    {name: "Web tech.", grade: "A+"},
    {name: "Soft. Eng.", grade: "A"},
    {name: "Calculus", grade: "B"},
    ]
    res.render("example");
}); 
```

```txt
List of Exams
Web tech. grade A+
Soft. Eng. grade A
Calculus grade B 
```

```txt
//- file: /views/example.pug
doctype html
html
    head
    title List of Exams
    body
    h1 List of Exams
    each exam in items
    li #{exam.name} grade #{exam.grade} 
```

## EXPRESS: THE REQUEST-RESPONSE CYCLE

## • The Request-Response cycle is the core of the Express framewor

## HTTP Request

## HTTP Response

## Express App

1. Create a requestand response object 

2. Performa sequence of one or more computationsteps to process the request 

• parse requestbody 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/54c6cae737bf1985f450daf0f5efc4d6ffad69c7c295bc54ef349b0e726e5d90.jpg)


• parse cookies 

• estabilish a session 

3. Prepareand send the response 

## EXPRESS: THE REQUEST-RESPONSE CYCLE

## • The Request-Response cycle is the core of the Express framewor

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/8b7d70bd0520e49d5795f578457d0ba9481a928bd5b1f56b7345261090cd0989.jpg)


## MIDDLEWARES

• In Express, middlewaresare functions thatcan manipulatethe curren requestand response objector executeany arbitrarycode 

• They’recalled thatbecause theyare executedin betweenreceivinga requestand sending back its response 

• Middlewares are executedin the same ordertheyare declaredin 

• They are functions thattake as input arguments: 

• req (the HTTP requestobject) and res (the HTTP response object) 

• next (a callback functionthat calls the next middleware in the stack) 

## OUR FIRST EXPRESS MIDDLEWARE

```javascript
// defined in some module
export function logger(req, res, next) {
    console.log("LOGGER HAS BEEN CALLED!");
    next();
} 
```

```javascript
// index.js file starting the express app
app.use(logging); // mounts the middleware function "logger" in the "/" path

app.get('/', (req, res) => {
    res.send('Hello World!')
});

app.listen(PORT); 
```

logger 

res.send("Hello World!" 

## OUR FIRST EXPRESS MIDDLEWARE

```javascript
// defined in some module
export function addTimestamp(req, res, next){
    req.timestamp = new Date();
    next();
} 
```

```javascript
// index.js file starting the express app
app.use(addTimestamp);
app.use(LOGger); // mounts the middleware function "logger" in the "/" path

app.get('/', (req, res) => {
    res.send(`Request received at ${req.timestamp}')
});

app.listen(PORT); 
```

## EXPRESS: THE REQUEST-RESPONSE CYCLE

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/bcbe26b833f33d4feb8b9900305226b10fdf8ecc063e160157b6fc637a362efa.jpg)


## HANDLING ERRORS

• It’s importantto make sure that any erroroccurring whenprocessing middlewares or routesis properlyhandledby Express. 

• If an erroris thrownduringsynchronouscode executionit will be automaticallycaught by the Express default errorhandle 

```javascript
app.get("/error", (req, res) => {
    throw new Error("An error occurred");
}); 
```

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/0f8c186e67b6a5249f6d4758ff04cbe424b3524629a521f69f5d0afa83c790a3.jpg)


## HANDLING ERRORS

• Errors returnedfrom asynchronousfunctions invokedby routehandlers and middlewares must be passed to the next() function 

```javascript
app.get('/readfile', (req, res, next) => {
    fs.readFile('/file-does-not-exist', (err, data) => {
    if (err) {
    next(err) // Pass errors to Express.
    } else {
    res.send(data)
    }
    })
}); 
```

## HANDLING ERRORS (IN EXPRESS 5)

• Starting from Express 5, routehandlersand middlewares thatreturna promise will automaticallycall next(value) whentheyrejector throwan error. 

• So, we won’tneedto do it explicitly 

```typescript
app.get('/user/:id', async (req, res, next) => {
    const user = await getUserById(req.params.id)
    res.send(user)
}) 
```

## ERROR HANDLERS

• Express includes a default errorhandler. The default handlerprints the entirestack trace onlywhenin developmentmode. 

• Wecan definecustom errorhandlersas wel 

• They are special middlewares with four input parameters 

```javascript
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
}); 
```

```txt
localhost:3000/error
← → ↙ localhost:3000/error ☆ ↗ >> ≡
Something broke! 
```

## USEFUL MIDDLEWARE

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/632c1528a387fd8ba3216d4eca56acf0758f9b862005593f21e056800d585e44.jpg)


## EXPRESS.STATIC

## express.static is a built-in middleware designed to serve static files

```javascript
// Register the built-in express.static middleware to serve static files.
// All files in the /public directory will be served as static files.
app.use(express.static("public")); // mounted in root "/"
app.use("/static", express.static("public")); // mount in virtual path "/static" 
```

• Uses req.urlto determine whethera requestmatches a file or paththe specified root directory (e.g.: public) 

## EXPRESS.URLENCODED

## express.urlencodedis a built-in middleware thatparses the body o incoming requests with urlencodedpayloads

```javascript
// Parses url-encoded body (e.g.: those in requests submitted via forms)
// and makes the parameters available in the req.body object.
app.use(express.urlencoded({extended: false})

app.get("/form", (req, res) => { res.render("form");});

app.post("/form", (req, res) => {
    res.send(`msg=${req.body.msg}; num=${req.body.num}`);
}); 
```

```julia
h1 Form
form(action="/form" method="POST")
input(type="text" name="msg")
input(type="number" name="num")
input(type="submit") 
```

## EXPRESS.JSON

express.json is a built-in middleware. Behaves similarly to express.urlencoded, butis designed to parse JSON requestbodies. 

```javascript
app.use(express.json());
app.post("/json", (req, res) => {
    res.send(`exam=${req.body.exam}; grade=${req.body.grade}`);
}) 
```

```html
POST http://localhost:3000/json HTTP/1.1
Content-Type: application/json
{
    "exam": "Web Technologies",
    "grade": "A+"
}
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 31
exam=Web Technologies; grade=A+ 
```

## EXPRESS-SESSION

express-session is a middleware available throughnpm 

• It simplifies the management of a server-stored session 

• Session data is stored on the server, session id is stored in a cookie 

• Notice: the default server-side storage is not production ready! Fo production, you should setup a dedicatedsession store (e.g.: memcachedor redis-based). 

## EXPRESS-SESSION: EXAMPLE

```javascript
app.use(session({
    secret: "s3cr37", saveUninitialized: false, resave: false
});

app.get("/session-counter", (req, res) => {
    if (!req.session?.count) {
    req.session.count = 1;
    res.send("It's the first time you visit this page.");
    } else {
    req.session.count = req.session.count + 1;
    res.send('You visited this page ${req.session.count} times.');
    }
}); 
```

## COOKIE-PARSER

• cookie-parser is a middleware available throughnpm 

• It parses the Cookie headerin incoming requests, and populates req.cookies with an object whose propertiesare the cookie name 

```javascript
app.use(cookieParser());
app.get("/cookie-counter", (req, res) => {
    if(! req.cookies?.count){
    res.cookie("count", 1, {maxAge: 10*60*1000});
    res.send("It's the first time you visit this page.");
    } else {
    res.cookie("count", parseInt(req.cookies.count) + 1, {maxAge: 10*60*1000});
    res.send(`You visited this page ${parseInt(req.cookies.count) + 1} times頁);
    }
});
```

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/edc480e87dfe77b7ab96c2deefe5974718a4cdfb39005b6bd8dfbd4f36e36999.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/69039feaa3367408ba11a1fc44b6f2ee9ea0933a439a6674399cd83246940dac.jpg)


## FLASH MESSAGES

• Often, in web applications, users are redirectedafter performingsome action (e.g.: redirectto homepage after deletingsome data). 

• It’s a good rule of thumbto providesome feedback to users in these cases , so theyknow whetherthe operationtheyperformedwas successful or not. 

• The «difficult» part is that, after redirecting, a whole new request-response cycle starts. How to keep track of the fact thatwe needto show some flash message? 

Success: App successfully reset 

A simple web app built using Node.js 20.9.0and Express 4.18.2.Source code and Docker environment available on Github. 

Beware: This web app is intended as a basic first example to showcase the express framework. It may contain security vulnerabilities and is definitely not production-ready! 

Manage your To-do List 

## FLASH MESSAGES

• Differentvariationof the same old problemof HTTP being stateless 

• Wecan solve this in the same ways we did before: cookies, sessions… 

• Some middlewares can be quiteuseful at that! 

• One such exampleis connect-flash, available on npm 

```javascript
import flash from "connect-flash"; //simple middleware for flash messages
app.use(flash()); //register the middleware 
```

## FLASH MESSAGES: EXAMPLE

```javascript
app.use(flash());
app.get("/redirect", (req, res) => {
    req.flash("info", "You have been redirected."); // Saves flash messages
    req.flash("info", "This is a demo to demonstrate flash messages.");
    req.flash("success", "Everything was fine.");
    req.flash("error", "But we also have an error message.");
    res.redirect("/showflash");
})
app.get("/showflash", (req, res) => {
    let infos = req.flash("info"); // Consumes flash messages with the given key
    let successes = req.flash("success");
    let errors = req.flash("error");
    res.render("flash", {infos: infos, successes: successes, errors: errors});
}) 
```

## FLASH MESSAGES: EXAMPLE

```txt
ul
each info in infos
li(style="color: blue") #{info}
each success in successes
li(style="color: green") #{success}
each error in errors
li(style="color: red") #{error} 
```

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/8b41ae472237a2e6fe28ee75e3e9b42c4c02434cefcd47e5f47f854c15ec84e7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/f4580c2439481cca5756b586c49f0f10e44024f6c7a74639d3b0256e3d84de5a.jpg)


## Flash messages demonstration

This is a page to demonstrate flash messages. Try to reload the page after being redirected here 

• You have been redirected 

• This is a demo to demonstrate flash messages. 

• Everything was fine. 

• But we also have an error message. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-10-29/41686374-1ac3-4b01-8a03-c98d0158e97c/91f1f2b70988115e7654d437133c10889b1bc01440a577c6d16b362077639491.jpg)


## FLASH MESSAGES: EXAMPLE

• If we reloadthe /showflash page (or visit it directlywithoutbeing redirectedby the /redirect page, no flash message will be stored in the currentsession, and we get: 

## Flash messages demonstration

This is a page to demonstrate flash messages. Try to reload the page after being redirected here. 

## SOURCE CODE AVAILABILITY

• The code in these slides is available in the Course Materialson Teams • You should check the code out, run(and debug) the web ap 

• Feel free to experimentwith middleware, change things around, and see what happens! 

## REFERENCES

## • Express web framework (Node.js/JavaScrip MDN web docs https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs

## • Inversionof Contro

By Martin Fowle https://martinfowler.com/bliki/InversionOfControl.ht 

## • Express Guide

Official Express website https://expressjs.com/en/guide/routing.ht https://expressjs.com/en/guide/writing-middleware.htm https://expressjs.com/en/guide/using-middleware.htm https://expressjs.com/en/guide/using-template-engines.html https://expressjs.com/en/guide/error-handling.htm 