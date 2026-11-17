# TYPESCRIPT: JAVASCRIPT WITH SYNTAX FOR TYPES

Luigi Libero Lucio Starace, PhD 

luigiliberolucio.starace@unina. 

https://luistar.github.i 

https://www.docenti.unina.it/luigiliberolucio.stara 

## JAVASCRIPT AND TYPES

JavaScript features a peculiartypesystem we learnedto love accept • It is dynamicallytyped 

```javascript
let x;
console.log(typeof(x)); //undefined
x = 1.25e7;
console.log(typeof(x)); //number
x = "Hello Web Technologies!";
console.log(typeof(x)); //string 
```

• It is also weaklytypedand loves performingimplicit casts 

```rust
let y = "100" - 1 + "42"; //string - number -> number, number + string -> string console.log(`${y}: ${typeof(y)}`); //9942: string 
```

## JAVASCRIPT AND TYPES

• These characteristics make the language practical for small web page manipulationtasks 

• It just works, no need to be verbose, declaring types or explicit casts 

• However, as the complexityof the programs grows: 

• It’s easier to introduce tricky bugs 

• Not the best developer experience(little IDE support, veryfew errors caught in the IDE and not at runtime) 

• Code becomes less maintainableand hard to understand 

## JAVASCRIPT: DAILY DEVELOPMENT TALES

```javascript
let message = "Hello Web Technologies!";
console.log(message.toLowerCase()); //hello web technologies!
message(); //TypeError: message is not a function (at runtime)

let employee = {name: "Jordan Belfort", role: "Stockbroker"};
employee.nome = "The Wolf of Wall Street"; //no error at all
console.log(employee.name); //Jordan Belfort

let team = ["Jordan Belfort", "Donnie Azoff", "Chester Ming"];
team.add("Nicky 'Rugrat' Koskoff"); //TypeError: team.add is not a function
console.log(team); 
```

It would be nice if we could catch these bugs beforeruntime! 

## TRANSPILERS

• JS started being used also for increasingly complex programs 

• Developers felt the need to address these limitations 

• JS was alreadywidelysupported, a new language was not feasible 

• Lots of new languages thatcompiledto standard JS poppedup! • CoffeeScript, TypeScript, Dart, Elm, … (~350 more are listed on this page) 

Code writtenin a new Programming Language, with additionalfancy features 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/8acec839-8c30-4b81-ab49-f8cc14bbf59b/0a35be02c120f5a5abba692d8d2fe46d98a6b99862702c2723b186b194a70d6a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/8acec839-8c30-4b81-ab49-f8cc14bbf59b/526dc9f597ab9dd934f2e495f7422195aae8ffe873b6796f6b39dbb97246cc89.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/8acec839-8c30-4b81-ab49-f8cc14bbf59b/bcb1f0fe924d801317cf089fa7fecae06b3d2df7f7a399c2a6ffc313eab89c4d.jpg)


JavaScript code (can runanywhere JavaScript runs) 

## TYPESCRIPT

• Born in 2012, designed and developedby Microsoft 

• Core dev: Anders Hejlsberg 

• Superset of JavaScript 

• … with static typing and more! 

• Compiles to JavaScript 

• By far, the most popularJS flavor 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/8acec839-8c30-4b81-ab49-f8cc14bbf59b/abf9c4c9262b5e5a0215bae353fb49e53f49194eef21933148ced1ee4c5fe54d.jpg)


## TYPESCRIPT: ADOPTION

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/8acec839-8c30-4b81-ab49-f8cc14bbf59b/00a41b4c1623d47040356f89376e67ab9e13a1ecaa7818728401ddd5880dded1.jpg)



From the State of JavaScript 2022 surve


## INSTALLING TYPESCRIPT

## TypeScript can be installed as an npmpackage

@luigi ➜ D/O/T/W/2/e/TypeScript $ npm install -g typescript 

added 1 package in 9s 

• The abovecommandmakes the tsc compilerglobally available 

• You can use npx or similar tools to runtsc from a local node_modules package 

• TypeScript files typically have a .ts extension 

## HELLO TYPESCRIPT

```javascript
// hello.ts file
// This is an industrial-grade general-purpose greeter function:
function greet(entity, date) {
    console.log(`Hello ${entity}, today is ${date}!`);
}
greet("Web Technologies"); 
```

• Standard JavaScript code is also valid TypeScript code 

• Wecan runthe above script as a plain JavaScript file with Node.js 

```txt
@luigi → D/O/T/W/2/e/TypeScript $ node hello.ts
Hello Web Technologies, today is undefined! 
```

## • Looks like we forgot the second parameter!

## HELLO TYPESCRIPT

## Whatif we try to compile hello.ts with tsc?

@luigi ➜ D/O/T/W/2/e/TypeScript $ tsc hello.ts --strict false 

hello.ts:6:1 - error TS2554: Expected 2 arguments, but got 1. 

6 greet("Web Technologies"); ~~~~~~~~~~~~~~~~~~~~~~~~~ 

hello.ts:2:24 2 function greet(person, date) { An argument for 'date' was not provided. 

Found 1 error in hello.ts:6 

## HELLO TYPESCRIPT

• The TypeScript compilerdetectedthe bug 

• ..eventhoughwe’veonly writtenstandard JavaScript code so far! 

## • Let’s fix the bug

```javascript
// hello.ts file
// This is an industrial-grade general-purpose greeter function:
function greet(entity, date) {
    console.log(`Hello ${entity}, today is ${date}!`);
}
greet("Web Technologies", Date()); 
```

## HELLO TYPESCRIPT

@luigi ➜ D/O/T/W/2/e/TypeScript $ ls –n hello.ts 

@luigi ➜ D/O/T/W/2/e/TypeScript $ tsc hello.ts --strict false 

@luigi ➜ D/O/T/W/2/e/TypeScript $ ls –n hello.js hello.ts 

@luigi ➜ D/O/T/W/2/e/TypeScript $ node hello.js Hello Web Technologies, today is Mon Dec 18 2023 09:33:18! 

## The tsc compiler transpiledhello.ts to the newly-created hello.js, which can be executed with Node as usua

## HELLO TYPESCRIPT: GENERATED CODE

hello.ts 

```javascript
// This is an industrial-grade general-purpose greeter function:
function greet(entity, date) {
    console.log(`Hello ${entity}, today is ${date}!`);
}
greet("Web Technologies", Date()); 
```

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/8acec839-8c30-4b81-ab49-f8cc14bbf59b/05d90c2d2f626e68a50bff7d3ee889cc1a8120b0140ecf3e7844dd56cd6e4e72.jpg)


hello.js 

```javascript
// This is an industrial-grade general-purpose greeter function:
function greet(entity, date) {
    console.log("Hello ".concat(entity, ", today is " ).concat(date, " !"));
}
greet("Web Technologies", Date()); 
```

## TYPESCRIPT: DOWNLEVELING

• tsc preservedcommentsand indentations. Transpiled code looks like it has beenwrittenby a human 

• The template string was changed to multiple .concat() invocations 

• Whyis that? 

• Template strings are an ES6 feature, and, by default, TS targets ES3 (1999 

• TS can rewritecode from newerversions to olderones (downleveling) 

• Wecan still use the nice new features, butourcode can runalso on old browsers supportingonly ES3! 

ES6 Code 

tsc 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/8acec839-8c30-4b81-ab49-f8cc14bbf59b/9ac90b68f4d748ccc7cc0c12980caa6bd84aefe1c53142d52688111374ec4b99.jpg)


ES3 Code 

Luigi Libero Lucio Starace, Ph.D. - University of Naples Federico II - Web Technologies Course - Lecture 24 - TypeScript 

## TYPESCRIPT: DOWNLEVELING

## • Whencompiling with tsc, we can specify the target version to use

@luigi ➜ D/O/T/W/2/e/TypeScript $ tsc –target es6 hello.ts 

## • The above commandcompiles the TS file to ES6 JavaScript

```javascript
// This is an industrial-grade general-purpose greeter function:
function greet(entity, date) {
    console.log(`Hello ${entity}, today is ${date}!`);
}
greet("Web Technologies", Date()); 
```

## TYPESCRIPT: DECLARING TYPES

• So far, we’veonly writtenplain old JavaScript code 

• TS allows us to declare types for variables, params and returnvalues 

• The most common primitive types in TS are string, number, boolean 

```typescript
primitive_types.ts
let courseName: string = "Web Technologies";
let credits: number = 6;
let isGreat: boolean = true;

console.log(
    Welcome to ${courseName}!
    Credits: ${credits} ETCS
    Status: ${isGreat ? "Great" : "Could be better"}
); 
```

## TYPESCRIPT: DECLARING TYPES

```typescript
let courseName: string = "Web Technologies";
let credits: number = 6;
let isGreat: boolean = true;

console.log(/* Omitted for the sake of brevity */); 
```

primitive_types.ts 

## • The aboveexampleis notvalid JavaScript code anymore!

```txt
@luigi → D/O/T/W/2/e/TypeScript $ node .\primitive_types.ts
D:\...\primitive_types.ts:1
let courseName: string = "Web Technologies";
^
SyntaxError: Unexpected token ':' 
Node.js v22.14.0 
```

## TYPESCRIPT: DECLARING TYPES

• To executeourexample, we must compile the TS file beforehand 

@luigi ➜ D/O/T/W/2/e/TypeScript $ tsc .\primitive_types.ts @luigi ➜ D/O/T/W/2/e/TypeScript $ node .\primitive_types.js 

Welcome to Web Technologies! 

Credits: 6 ETCS 

Status: Great 

@luigi ➜ D/O/T/W/2/e/TypeScript $ 

## TYPESCRIPT: ENJOYING TYPE CHECKING!

primitive_types.t 

```rust
let courseName: string = "Web Technologies";
let credits: number = 6;
let isGreat: boolean = true;
credits = "9 CFU"; // This would be fine in plain JavaScript! 
```

```txt
@luigi → D/O/T/W/2/e/TypeScript $ tsc .\primitive_types.ts
primitive_types.ts:5:1 - error TS2322: Type 'string' is not assignable to type
'number'. 
```

5 credits = "9 CFU"; 

Found 1 error in primitive_types.ts:5 

## TYPESCRIPT: ARRAY TYPES

## To specify the typeof an array, we can use the syntax type[]

array.ts 

```typescript
let langs: string[] = ["TypeScript", "JavaScript", "PHP", "Java"];  
let primes: number[] = [2, 5, 7, 97, 829, 839];  
langs.push({name: "C#"}); //would be fine in plain JavaScript 
```

@luigi ➜ D/O/T/W/2/e/TypeScript $ tsc .\array.ts array.ts:4:12 - error TS2345: Argument of type '{ name: string; }' is not assignable to parameter of type 'string'. 

4 langs.push({name: "C#"}); //would be fine in plain JavaScript 

Found 1 error in array.ts:5 

## TYPESCRIPT: THE ANY TYPE

• TypeScript includes a special type: any 

• Whena value is of typeany, we can do anythingwith it and the compiler won’tcomplain! 

• The code belowcompiles fine 

• …and throwsa TypeError: x.foo is not a function 

```txt
let x: any;
x = {name: "Angular", lang: "TypeScript"};
x.foo();
x = "Hello!";
let n:number = x; 
```

## TYPESCRIPT: WORKING WITH FUNCTIONS

• TypeScript allows us to specify the types of boththe inputs and outpu values of functions 

```typescript
function greet(name: string): string {
    return `Hello ${name.toUpperCase()}`;
}

console.log(greet(42));
//Err. TS2345: Arg. of type 'number' is not assignable to param. of type 'string' 
```

## TYPESCRIPT: AUTOMATIC TYPE INFERENCE

• Whenno explicit typeannotationis provided, TypeScript tries to automaticallyinfer types from the context 

• In modernTS, the automaticinferenceof any raises an error(unless you compile with the option -- strict false) 

```typescript
function greet(name){ //function greet(name: any): string
    return `Hello ${name}`;
}

let arr = [1,2,3,4,5]; //let arr: number[]

let course = "Web Technologies"; //let course: string
greet(course);

course = {name: "Web Technologies", credits: 6};
//TS2322: Type '{name: string; credits: number;}' not assignable to type 'string' 
```

## TYPESCRIPT: IMPLICIT ANY

• When you don’t specify a type, and TypeScript can’t infer it from context, the compiler in older TS versions typically defaulted to any. 

• We might want to avoid this, because any isn’t type-checked. 

• The compiler flag noImplicitAnycan be used to flag any implicit any as an error. 

implicit_any.ts 

```typescript
let x; //let x: any
function greet(name){ //function greet(name: any): void console.log('Hello, ${name}');}
greet(x); 
```

## TYPESCRIPT: IMPLICIT ANY

```typescript
let x; //let x: any
function greet(name){ //function greet(name: any): void console.log('Hello, ${name}');}
greet(x); 
```

implicit_any.ts 

```txt
@luigi → D/O/T/W/2/e/TypeScript $ tsc .\implicit_any.ts
@luigi → D/O/T/W/2/e/TypeScript $ tsc -noImplicitAny .\implicit_any.ts
implicit_any.ts:3:16 - error TS7006: Param 'name' implicitly has an 'any' type.
3 function greet(name){ //function greet(name: any) : string
~~~~~~
Found 1 error in implicit_any.ts:3 
```

## TYPESCRIPT: OBJECT TYPES

## To define an object type, we list its propertiesand theirtype

```typescript
function printCourse(course: {name: string, credits: number}) {
    console.log(`Course name: ${course.name}`);
    console.log(`Course credits: ${course.credits}`);
}

printCourse({name: "Web Technologies", credits: 6}); //works fine

printCourse({name: "Software Engineering"}); //compile error
// TS2453: Property 'credits' is missing in type '{ name: string; }' but required
// in type '{ name: string; credits: number; }'

printCourse({name: "Algebra", credits: 6, year: "First"}); //compile error
// TS2353: Object literal may only specify known properties, and 'year' does not
// exist in type '{ name: string; credits: number; }' 
```

## TYPESCRIPT: OPTIONAL PROPERTIES

## Object types can specify one or more optionalproperties, by adding a «?» after the propertyname

```typescript
function printCourse(course: {name: string, credits?: number}) {
    console.log(`Course name: ${course.name}`);
    console.log(`Course credits: ${course.credits}`);
    //we should check whether course.credits is undefined!
}

printCourse({name: "Web Technologies", credits: 6}); //works fine
printCourse({name: "Software Engineering"}); //works fine
//prints "Course credits: undefined"!

printCourse({name: "Algebra", credits: 6, year: "First"}); //compile error
// TS2353: Object literal may only specify known properties, and 'year' does not
// exist in type '{name: string; credits: number;} 
```

## TYPESCRIPT: UNION TYPES

• Union types are obtainedby combiningtwoor more types 

• Combinedtypes are definedusing a list of types separatedby «| 

• Representvalues that can belongto any of the combinedtypes 

```typescript
function printError(code: number | string){
    console.log(`Error code: ${code}`);
}

printError(404);
printError("401 Unauthorized");
printError({code: "403", message: "Forbidden"}); // compile error
// TS2345: Argument of type '{ code: string; message: string; }' is not
// assignable to parameter of type 'string | number' 
```

## TYPESCRIPT: WORKING WITH UNION TYPES

## • TypeScript ensures thatoperationson a union typeare valid on each possible typein the union union ts union.ts

```typescript
function printError(code: number | string){
    console.log(`Error code: ${code.toUpperCase()}`);
    // compile error
} 
```

@luigi ➜ D/O/T/W/2/e/TypeScript $ tsc .\union.ts union.ts:2:35 - error TS2339: Property 'toUpperCase' does not exist on type 'string | number'. Property 'toUpperCase' does not exist on type 'number'. 

2 console.log(`Error code: ${code.toUpperCase()}`); 

Found 1 error in union.ts:2 

## TYPESCRIPT: WORKING WITH UNION TYPES

• In such cases , we needto narrowdown the typefor TypeScript using code and specific checks (e.g.: using typeof, or Array.isArray(x)) 

• TypeScript can infer specific types for particularbranches 

union.ts 

```typescript
function printError(code: number | string){
    if(typeof code === "string") {
    console.log(`Error: ${code.toUpperCase()}`); //in this branch code: string
    } else {
    console.log(`Error: ${code}`); //in this one code: number!
    }
} 
```

## TYPESCRIPT: TYPE ALIASES

• We’vebeenusing Object types and Union types by specifying them directlyin typeannotations 

• Wemight wantto use the same types multiple times 

• As Software Engineers we wantto writeDRY (Don’tRepeatYourself) code! 

• Type aliases are a way to assign a specific name to a type 

• The syntax for a typealias involves using the typekeyword 

$$
\text { type } \quad <   \text { name } > = <   \text { definition } >
$$

## TYPESCRIPT: TYPE ALIASES

```typescript
type Credits = number | string;
type Course = {
    name: string,
    credits: Credits
}

function printCourse(course: Course) {
    console.log(`Course name: ${course.name}`);
    console.log(`Course credits: ${course.credits}`);
}

let webtech: Course = {name: "Web Technologies", credits: 6};
let softeng: Course = {name: "Software Engineering", credits: "10 CFU"};
printCourse(webtech); //Name: Web Technologies, Credits: 6
printCourse(softeng); //Name: Software Engineering, Credits: 10 CFU 
```

## TYPESCRIPT: INTERFACES

• Interface declarations are anotherway of naming object types 

```typescript
interface Course {
    name: string;
    credits: number;
}
function printCourse(course: Course) {
    console.log(`Name: ${course.name}, Credits: ${course.credits}`);
}
let webtech: Course = {name: "Web Technologies", credits: 6};

printCourse(webtech);
printCourse({name: "Software Engineering", credits: 10}); 
```

## TYPESCRIPT: STRUCTURALLY TYPED NATURE

## TypeScript is a structurally-typedlanguage

• It only cares aboutstructureand capabilities of types whendeterminingtype compatibility, not aboutnames! 

• Java, on the contrary, features a nominative typesystem. 

```typescript
interface Person { name: string; age: number; }
interface Pet { name: string, age: number }

function printPerson(p: Person) { console.log(`Name: ${p.name}, age: ${p.age}`);}

let person: Person = {name: "Janet", age: 20};
let pet: Pet = {name: "Chuck", age: 3};

printPerson(person); //Name: Janet, age: 20
printPerson(pet); //Name: Chuck, age: 3 
```

[1] Paquet, J., & Mokhov, S. A. (2010). Comparative studies of programming languages; course lecture note Section 3.3. arXivpreprint: https://arxiv.org/pdf/1007.2123.p 

## TYPESCRIPT: EXTENDING INTERFACES

```typescript
interface Pet {
    name: string
}

interface Bird extends Pet {
    flies: boolean
}

let chuck: Bird = {name: "Chuck", flies: true};
let quentin: Bird = {flies: false}; // compile error
// TS2322: Type '{ flies: false; }' is not assignable to type 'Bird'.
// Property 'name' is missing in type '{ flies: false; }' but required in type
// 'Pet'. 
```

## TYPESCRIPT: TYPES VS INTERFACES

## Type aliases and interfaces are verysimilar and ofteninterchangeable

• A key distinctionis thattypes cannotbe re-openedto add new properties, whileinterfaces are always extendable 

```typescript
interface Pet {
    name: string
}

interface Pet {
    age: number
}

let matt: Pet = {name: "Matt", age: 2}; 
```

```typescript
type Pet = {
    name: string
}

type Pet = { //TS2300: Dup. identifier
    age: number
}

let matt: Pet = {name: "Matt", age: 2}; 
```

## TYPESCRIPT: EXTENDING TYPE ALIASES

```typescript
type Pet = {
    name: string
}

type Bird = Pet & { //intersection type!
    flies: boolean
}

let chuck: Bird = {name: "Chuck", flies: true}; 
```

• Similarly to Union types, Intersectiontypes combine multiple types into one. Createdusing the «&» character. 

• The resultingtypehas the propertiesof each single type 

## TYPESCRIPT: TYPE ASSERTIONS

• Sometimes, as a dev, you will know betterthanTypeScript! 

• For example, if you use document.getElementById(), TypeScript will only be able to infer thatthe call will returnan HTMLElement. 

• But you might know thatthe particularelementwill be of a more specific type! 

const nameInput = document.getElementById("name") as HTMLInputElement; 

## • Beware: not really an assertion (as in the testing domain) • Not enforcedat all at runtime, just at compile-time!

## TYPESCRIPT: TYPE LITERALS

In additionto string and numbertypes, we can referto specific strings and numbersin typepositions 

```txt
let alignment: "center";
alignment = "center";
alignment = "left"; //TS2322: Type ''left'' is not assignable to type ''center'' 
```

• In the example, alignment can only have the center value 

• That’s not veryuseful… 

• Literals can be combinedwith Unionsto express a much more useful concept: types thatcorrespondto a certainset of know values! 

## TYPESCRIPT: TYPE LITERALS

```typescript
type Alignment = "center" | "left" | "right";
let alignment: Alignment;
alignment = "left"; //ok
alignment = "right"; //ok
alignment = "centre"; //compile error
// TS2820: Type ''centre'' is not assignable to type 'Alignment'.
// Did you mean ''center''? 
```

## TYPESCRIPT: ENUMS

## Enums allow developers to definea set of named constants

```typescript
interface Order{ isPremium: boolean }

enum Priority {
    Low,
    Medium,
    High
}

function computePriority(s: Order): Priority {
    if(s.isPremium)
    return Priority.High;
    return Priority.Low;
}

console.log(Priority.Medium); //1 
```

## TYPESCRIPT: FUNCTION TYPES

• Whatif we wantto specify thata functiontakes as input a callback whichexpects specific parametersand produces a given output? 

• Functions can be described using functiontypeexpressions 

```typescript
type stringDecoratorFunction = (x: string, mode: boolean) => string; 
```

• The functiontypeaboveindicates a functionthattakes as inputs a string and a booleanargument, and returnsa string 

```typescript
let fn: () => string; //fn is a function that takes no args and returns a string
fn = () => {return "Hello Web Tech"};    //ok
fn = (x: string) => {return `Hello ${x}`} //TypeError! 
```

## TYPESCRIPT: FUNCTION TYPES

```typescript
enum Case { Uppercase, Lowercase }

function GREET(name: string, decorator: (x: string, mode: Case) => string){
    return decorator(name, Case.Uppercase);
}

function stringDecorator(x: string, mode: Case) {
    if(mode === Case.Lowercase)
    return `>>> Hello ${x} <<'.toLowerCase();
    else
    return `>>> Hello ${x} <<'.toUpperCase();
}

console.log(GREET("Web Technologies", stringDecorator)); 
```

## GENERICS

• A good deal of efforts in Software Engineering goes towardsbuilding reusablesoftware 

• Developing components that ca seamlessly operate on both curren and future data is crucial for buildin up large software systems 

• Generics is one of the main tools t write code that can seamlessly wor with a variety of type 

## HELLO GENERICS: THE IDENTITY FUNCTION

Suppose we needto implementthe identityfunction, i.e., a functionthat returnsback whatever is passed in. 

```typescript
function identity(x){ //function identity(x: any): any return x;
}
let y: string = "Hello";
let z = identity(y); //z: any! 
```

• Using any (implicitly or explicitly) is certainlygeneric enough 

• But we’re loosing information aboutwhatthe typewas whenthe functionreturns! 

## HELLO GENERICS: THE IDENTITY FUNCTION

```typescript
function identity(x: string): string {
    return x;
}

let y: string = "Hello";
let z = identity(y); //z: string (but only works with string!) 
```

Wecould give the identityfunctiona specific type 

• It wouldonly work with strings though… 

## TYPESCRIPT: GENERICS

TypeScript allows us to definetypevariables, a special kind of variables thatworks on types ratherthanvalues 

• The typevariableis declaredafter the functionname, between«<» and «> 

• Below, the variableis called Type (butit could any valid identifieras a name). 

```typescript
function identity<Type>(x: Type): Type {
    return x;
}

let s: string = identity<string>("Hello"); //explicitly set Type to string
let n: number = identity(42); //let automatic type inference do its magic
let o: {title: string, artist: string} = identity({
    title: "Sultans of swing",
    artist: "Dire Straits"
}); 
```

## TYPESCRIPT: GENERICS

```typescript
function identity<Type>(x: Type): Type { return x; }

let s: string = identity<string>("Hello"); //explicitly set Type to string
let n: number = identity(42); //let automatic type inference do its magic
let o: {title: string, artist: string} = identity({
    title: "Sultans of swing", artist: "Dire Straits"
}); 
```

• This is not the same as using the any type 

• We’represervingthe information on the input type! 

## TYPESCRIPT: GENERICS

## • There can be multiple typevariables as well

```typescript
function merge<T1, T2>(x: T1, y: T2): {field: T2, otherField: T1} {
    return {field: y, otherField: x};
}

let x = merge("Sultans of Swing", 42);
//x has type {field: number, otherField: string} 
```

• And we can also work with type-parametricarrays 

```typescript
function getFirst<T>(arr: T[]): T {
    return arr[0];
}

let first: string = getFirst(["hello", "web", "technologies"]);
console.log(first); //hello 
```

Luigi Libero Lucio Starace, Ph.D. - University of Naples Federico II - Web Technologies Course - Lecture 24 - TypeScript 

## TYPESCRIPT: GENERIC CLASSES

```typescript
class CustomCollection<T> {
    list: T[] = [];
    addElement(element: T): number {
    return this.list.push(element);
    };
    getRandomElement(): T{
    let selectedIndex: number = Math.floor(Math.random() * this.list.length);
    return this.list[selectedIndex];
    }
}
let c = new CustomCollection<string>();
c.addElement("hello"); c.addElement("web"); c.addElement("technologies");
console.log(c.getRandomElement()); 
```

## TYPESCRIPT: GENERIC TYPE CONSTRAINTS

```typescript
class Animal { species: string; }
class Bird extends Animal { canFly: boolean; }
class Snake extends Animal { isVenomous: boolean; }

function animalInfo<T extends Animal>(animal: T): void {
    console.log(animal.species);
}

let a: Animal = new Animal(); a.species = "Dog";
let b: Bird = new Bird(); b.species = "Kiwi"; b.canFly = false;
let c: Snake = new Snake(); c.species = "Cobra"; c.isVenomous = true;

animalInfo(a); //Dog
animalInfo(b); //Kiwi
animalInfo(c); //Cobra
animalInfo({species: "Spider"}); //Spider (!!!) 
```

## TYPESCRIPT: OTHER TYPES TO KNOW ABOUT

TypeScript includes also some additionaltypes, thatmight be useful especially in the contextof functions, and thatwe should know about: 

• void 

• unknown 

• never 

## TYPESCRIPT: VOID

• void is the returntypeof functions thatdo not returna value 

• It is the inferredreturnvalue for functions thatdo not have a return statement, or have an emptyreturnstatement 

```typescript
function f(): void {
    return;
}

function g(){ // function g(): void console.log("Hello");
}

let x: void = g(); 
```

## TYPESCRIPT: UNKNOWN

• unknownrepresentsany possible value. 

• It is similar to the any type, but safer (does not allow any operation!) 

```typescript
function greet(a: any){
    console.log(a.name); //OK, but possible runtime error
}

function saferGreet(a: unknown){
    console.log(a.name); //Compile error TS18046: 'a' is of type unknown
}

type namedObject = {name: string};

function notSoSafeGreet(a: unknown){
    console.log((a as namedObject).name);
} 
```

## TYPESCRIPT: THE NEVER TYPE

## • Some functions neverreturna value

• The nevertyperepresentsvalues whichare neverobserved 

```typescript
function f(x: string | number){
    if(typeof x === "string") {
    return x.toLowerCase();
    } else if (typeof x === "number") {
    return x.toPrecision(2);
    } else {
    return x; //x has type never in this branch
    }
}

function g(x: any): never { //g never returns (it always throws an error)
    throw new Error("Oops!");
} 
```

## TYPESCRIPT: STRICTNESS LEVELS

• Differentusers expect differentthings from TypeScript 

• By default, TypeScript offers an opt-in experience 

• Types are optional, any is used whena precise typecannot be inferred 

• Wecan be more strict aboutinferredanys by using the noImplicitAnyflag 

• To avoid being too intrusive, some checks are disabled by default 

• For example, null and undefinedcan be assigned to any type 

• Forgettingto explicitly handle null/undefinedvalues is the cause of countless bugs in the world (some called it the billion dollar mistake!) 

• The strictNullChecks flag can be used to ensurethatnull and undefinedvalues are explicitly handled 

## TYPESCRIPT: STRICT NULL CHECKS

```typescript
class CustomCollection<T> {
    list: T[] = [];
    add: (x: T) => number = (element: T) => {
    return this.list.push(element);
    }
}

let x = new CustomCollection<string>();
x.add("Sam"); x.add("Cliff"); x.add("Mama");

let character = x.list.find((val: string) => {
    return val === "Amelie"
});

console.log(character.toUpperCase()); //character might be undefined! 
```

## TYPESCRIPT: STRICT NULL CHECKS

• ModernTS enables strict mode by defaul 

• Older versions had to specify the –strictNullChecks option 

@luigi ➜ D/O/T/W/2/e/TypeScript $ tsc -target es6 .\strict.ts --strict false 

@luigi ➜ D/O/T/W/2/e/TypeScript $ tsc -target es6 .\strict.ts @luigi ➜ D/O/T/W/2/e/TypeScript $ tsc -target es6 -strictNullChecks .\strict.ts strict.ts:13:13 - error TS18048: 'character' is possibly 'undefined'. 

13 console.log(character.toUpperCase()); 

~~~~~~~~~ 

Found 1 error in strict.ts:13 

## REFERENCES (1/2)

## • The TypeScript Handbook

Available at https://www.typescriptlang.org/docs/handbook/intro.ht 

You do not needto know the entirehandbook! Use it as a referencefor the parts thatwerediscussed in these slides. 

## • Lecture Notes for the Comparative Studies of Programmi Languages Course (Revision 1.9)

By Paquet, J., & Mokhov, S. A. (2010) 

Available at https://arxiv.org/pdf/1007.2123.pdf 

If you want to learn more about type system design in programming languages (e.g.: duck typing, struct vs nominative type systems), check out Section 3.3. This is notrequired for the Web Technologies cours 

## REFERENCES (2/2)

## To Type or Not to Type? A Systematic Comparison of the Softwa Quality of JavaScript and TypeScript Applications on GitHu

By Justus Bogner and Manuel Merkel (2022) 

Available at https://dl.acm.org/doi/pdf/10.1145/3524842.3528454 

Interesting read. The authors compare JavaScript and TypeScript applications on multiple grounds, rangi from code quality and readability to bug proneness and bug resolution tim 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/8acec839-8c30-4b81-ab49-f8cc14bbf59b/8e22774faadc7833e16da0725a77f4d846cc415a628904c11cafe51105ef9f7e.jpg)
