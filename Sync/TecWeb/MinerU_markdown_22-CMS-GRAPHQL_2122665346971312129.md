# (HEADLESS) CONTENT MANAGEMENT SYSTEMS AND GRAPHQL

Luigi Libero Lucio Starace, PhD 

luigiliberolucio.starace@unina. 

https://luistar.github.io; https://squids.unina.i 

https://www.docenti.unina.it/luigiliberolucio.stara 

## MANAGING CONTENT: CHALLENGES

The key goal of manyweb applications is to display contentto users 

• Content may change veryfrequentl 

• Content may growexponentially(e.g.: ~7M pages in Wikipedia) 

This poses some challenges: 

• Hand-coding entire web pages for content updates requires technic expertise and results in slower workflow 

• Those in charge of contents are typically not the web devs 

• Managing different versions of the published content is not triv 

• Ensuring a structured workflow is adopted is challengin 

## CONTENT MANAGEMENT SYSTEMS

• A Content Management System (CMS) is a web application designed allow collaborative editing, organizing and publishingof content 

• Without the need to write a single line of code, using the User Interf (UI) provided by the CMS itsel 

• Empowers non-technical users to manage and update content without consta reliance on web devs. 

• CMSs are often used to run blogs, news, and e-commerce websites 

## CMS: FEATURES

Most CMS include the following feature 

• Web publishing(e.g.: contentis available to users via web pages) 

• Formattingcontent(typicallywith a WYSIWYG graphical editor) 

• Version control(keep track of multiple versions of the same content) 

• Indexing, search and retrievalof content 

• User authentication/authorizationwith a group-based permission system 

• Built-in media manager for multimedia content 

• Extensibilityand customizability(via themes and plugins) 

## TRADITIONAL CMS ARCHITECTURE

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/e9a002637918bac0965739ac209340cc4f87e70fbcd7ea7e4d4e6b03bba65c6a.jpg)


Content Managemen Application (CMA) 

Content Delivery Application (CDA) 

TraditionalCMS are composed by twokey parts: 

• Content Management Application: allows non-technical users to manage content(e.g.: throughits web pages) 

• Content Delivery Application: Makes the updatedcontentavailable to end-users (e.g.: as web pages) 

Luigi Libero Lucio Starace, Ph.D. - University of Naples Federico II - Web Technologies Course - Lecture 22 - (Headless) CMSs an d GraphQ 

## TRADITIONAL CMSs

TraditionalCMS have a monolithicarchitecture 

• CMA and CDA are closely integratedin a monolith 

• This makes traditionalCMSs easy to distributeand operate (theyare a single web applicationwith twocomponents) 

These advantages come with some limitations: 

• Mightnotbe flexible enoughfor some needs 

• Mightlimit distributionchannels (traditionalCMSs generallyprioritize web outputs. Whatif I needto deploya REST API?) 

## HEADLESS CMSs

• Headless CMSs are a recenttrend 

• Based on the idea to separat 

• the CMA (the body, which takes care of contentorganization) and 

• the CDA (the head, which takes care of the presentation) 

• An Headless CMS is a CMS withoutits head. It does not manage the presentationof content, and only exposes an API 

• This way, contentcan be deployedon any channelwe need 

## DECOUPLED CMSs

• DecoupledCMSs are traditionalCMSs in whichthe CMA and the CDA are decoupled. 

• Users can use the includedCDA, or implementdifferentways to distributethe contentusing the APIs exposed by the CMA 

• Most TraditionalCMS are nowadaysdecoupled(e.g.: WordPress) 

## CMSs: OVERVIEW

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/cbde2b5ccb36a6e7d8d18515a6ff53c61b18b325577860ad6b3c4292b6af7887.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/3e3a9b22647917dad0ed2bbddafdb1db9064251f1be5e512865e3b950514d0d8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/0abb9002e3a5c99d4908e7a41efda72614f7666ab6c629aabba607874bc5e2c3.jpg)


## CMSs: SECURITY RISKS

• CMS are great targets for attacks 

• The same CMS is used on a large numberof websites 

• A vulnerabilityin a CMS can be exploitedon a large numberof websites 

• It is imperativeto keep CMSs updated to patc vulnerabilities as soon as possible 

• CVE-2022-21661 WordPress between versions 3.7.3 and 5.8.3 was vulnerable to SQL Injections! 

• CVE-2022-23797 Affects Joomla! 3.0.0–3.10.6 and 4.0.0–4.1.0 allowed unauthenticated remo attackers to execute arbitrary SQL querie 

• CVE-2026-119977 RCE in WordPress from 4.7 to 7.1. • Added November 03, 2026 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/79f152d057dd2ffe73370b37e2a740ca58e6c6fe35522182fe09f6a521d74e5f.jpg)


## USING A (TRADITIONAL) CMS

## TRADITIONAL CMS MARKET SHARE

• A numberof CMS exists (full list here). Well-knownones include: 

• WordPress(the most popularCMS) 

• Joomla (powers the website of the Computer Science courses at UniNA) 

• WooCommerce(e-commerce websites solution) 

• MediaWiki(powers Wikipedia, Fandom, WikiHow, 

• WordPress is the most widelyused (used by ~43% of all websites!) 

• Note thatsome of these (e.g.: WordPress) feature a decoupled architecture. 

## USING A (TRADITIONAL) CMS

• A traditionalCMS is typicallya web app as any other 

• In the initial install phase, it requiresthe user to specify the data necessary to connect to a relationaldatabase (e.g.: url, username password) 

• Uponconnection, it creates the necessary tables 

• Generally, duringthe install phase, the CMS asks the user to specify the credentials (username, password) for the administrationaccount 

• After install, the admin can create and organize content, add new users, definethe templates and customize the appearenceof the website, etc… Unauthorizedusers can access the content. 

## USING A (TRADITIONAL) CMS

• Let’s install WordPress (using Docker) and let’s check it out 

• Live demo time! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/421500197e2362ec2b86af77285ecada0d97d69e0ffc23a2f8124bc6139183a2.jpg)


## INSTALLING WORDPRESS

• Data for the connection to th database is passed via environmen variables (see compose.ymlfile) 

• Here is the web page wherewe specify the title of the website and we create an admin use 

<table><tr><td colspan="2">Benvenuto</td></tr><tr><td colspan="2">Benvenuto nella famosa installazione di WordPress in cinque minuti! Compila semplicemente le informazioni qua sotto e sarai già sulla strada per utilizzare la piattaforma di pubblicazione più estesa e potente del mondo.</td></tr><tr><td colspan="2">Informazioni necessarie</td></tr><tr><td colspan="2">Inserisci le seguenti informazioni. Non preoccuparti, potrai sempre cambiarle in seguito.</td></tr><tr><td>Titolo del sito</td><td>Web Technologies</td></tr><tr><td rowspan="2">Nome utente</td><td>luigi</td></tr><tr><td>I nomi utente possono essere composti soltanto da caratteri alfanumerici, spazi, trattini bassi, trattini, punti e il simbolo @.</td></tr><tr><td rowspan="3">Password</td><td rowspan="2">luigiVery weakNascondi</td></tr><tr></tr><tr><td>Importante: Avrai bisogno di questa password per accedere. Conservala in un posto sicuro.</td></tr><tr><td>Conferma password</td><td>Conferma l&#x27;uso di una password debole</td></tr><tr><td rowspan="2">La tua email</td><td>admin@admin.com</td></tr><tr><td>Controlla attentamente il tuo indirizzo email prima di continuare.</td></tr><tr><td>Visibilità ai motori di ricerca</td><td>Scoraggia i motori di ricerca dall&#x27;effettuare l&#x27;indicizzazione di questo sitoÈ compito dei motori di ricerca onorare o meno questa richiesta.</td></tr><tr><td colspan="2">Installa WordPress</td></tr></table>

## INSTALLING WORDPRESS

• Done. WordPress has beeninstalled. 

• Wecan nowlogin using the admin account we created. 

• An examplehomepage has been createdfor us. Wecan access it at http://localhos 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/18206e0de1707686ddc1ffa1a962ea911be0d0ef5167b7086c5172628fd756a3.jpg)


## Congratulazioni!

WordPress è stato installato. Grazie e buon divertimento 

Nome utente luigi 

Password La password che hai scelto. 

Accedi 

## WORDPRESS: ADMIN DASHBOARD

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/840bd9f5db179046df6125722f0617b852803fe87108d025859fe7335da7dac0.jpg)


## HEADLESS CMSs

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/7486d5e69ec5529d10d2faa9544c4f9d339996ffa2b9f6c502b8f1f13f93649d.jpg)


## HEADLESS CMS

PopularHeadless CMS include: 

• Strapi (based on Node.js) 

• Wagtails (based on the Django framework for Pytho 

• Ghost (also based on Node.js) 

• CrafterCMS(based on Java) 

## STRAPI: GETTING STARTED

@luigi ➜ D/O/T/W/2/e/1/strapi $ npx create-strapi-app@latest project-name 

@luigi ➜ D/O/T/W/2/e/1/strapi $ cd project-name 

@luigi ➜ D/O/T/W/2/e/1/strapi/project-name $ npm run develop 

## • npx create-strapi-app is the fastest way to get started

• A wizard will 

• Ask for some basic information aboutour project 

• Create an npmproject 

• Install dependencies 

## • npmrundevelopcan be executedto runthe Strapi app in dev mode

## STRAPI: GETTING STARTED

@luigi ➜ D/O/T/W/2/e/1/strapi/project-name $ npm run develop 

> todo-api@0.1.0 develop strapi develop 

Building build context (577ms) Creating admin (16224ms) Loading Strapi (1505ms) Generating types (1413ms) 

Welcome back! 

To manage your project , go to the administration panel at: http://localhost:1337/admin 

To access the server , go to: http://localhost:1337 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/c28d4fefc914e97471d0d0757c57a9e1a15ab2cb661c5e656272b565651e83a9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/8910172a97f47a3c63bec25bc8f3a9da36e972d085a13f1e0dd383215d6106af.jpg)


## STRAPI: CREATING THE ADMIN USER

## Welcome to Strapi!

Credentials are only used to authenticate in Strapi. All saved data will be stored in your database. 

First name* 

luigi 

Last name 

Email* 

admin@admin.com 

Password* 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/376289eddab319cd01cd23110218a83e1beeab7a43f5a44972c58462ce70cf78.jpg)


Must be at least 8 characters, 1 uppercase, 1 lowercase & 1 number 

Confirm Password* 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/0194a0bff3c576726b9780d30671e25e6a9d579de0737b0ee7abd0f4f0a8aa58.jpg)


Keep me updated about new features & upcoming improvements (by doing this you accept the termsand the privacy_policy) 

Let's start 

## STRAPI: ADMIN DASHBOARD

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/8149244bbbd201fb8979c8e4975480d45663c44a6c685d73053492f74ec7fa3c.jpg)


## STRAPI: CREATING RESOURCES

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/ed36a27a2376df48cc5f400bb8c313301e1672024987e34f658bfeb0951219a8.jpg)


## STRAPI: DEFINING RESOURCES

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/b4a452f1a573f29b84fc656e02b2dc34c63cbf6624eae7f98c3f79c0c6ed433d.jpg)


## STRAPI: DEFINING RESOURCES

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/cb32a22e3ed2aacd2bd97afb0db7c4c7c70b50cd55a85ce4a7a5751ab0313605.jpg)


## STRAPI: DEFINING RESOURCES

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/a5a55caae62f85147eba99aff6cd43b73f1ca4ad7b304892b7f15cf25785adae.jpg)


## STRAPI: DEFINING RESOURCES

## Add new Number field

Name 

credits 

No space is allowed for the name of the attribute 

BASIC SETTINGS ADVANCED SETTINGS 

Cancel 

## Number format

integer (ex: 10) 

Choose here 

integer (ex: 10) 

big integer (ex: 123456789) 

decimal (ex: 2.22) 

float (ex: 3.33333333) 

## STRAPI: DEFINING RESOURCES

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/eadffcb0c56770d88ea6bee38f23a021201aeeaf7cb4ba047a64fbb8f68835f0.jpg)


## STRAPI: RELATIONS BETWEEN RESOURCES

## • Strapi allows us to define relations betweenresources using the visual editor

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/4ec12462f4dcd15149e9b839a9a9faf6be85c649fc3dbae5e9ffc982f52e26f3.jpg)



Luigi Libero Lucio Starace, Ph.D. - University of Naples Federico II - Web Technologies Course - Lecture 22 - (Headless) CMSs and GraphQL


![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/59474d9c0178b5490fe8894f7fb53b8b53c6ba8ef5aa9a3ea2a99c5e3bef87bc.jpg)


## STRAPI: RELATIONS BETWEEN RESOURCES

## STRAPI: RELATIONS BETWEEN RESOURCES

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/e67a923be698dd4faab0af8ac6ffacb4c31528e1fca48f6c6a310a1e758167f8.jpg)


## STRAPI: CREATING CONTENT

• So far, we definedthe «shape» of the resources we wantto manage • Strapi allows us to create the actual content, using its GUI 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/6e58bd4b0412423a2f283b61ce915da8e2152091af6a375cea827fdbf13edb7f.jpg)


## STRAPI: CREATING CONTENT

## • So far, we definedthe «shape» of the resources we wantto manage

• Strapi allows us to create the actual content, using its GUI 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/00f6612063b031500b6a8fff167bb16f54f2eaff1fa3a7c8bf41f2ec900e120b.jpg)


## STRAPI: MANAGING CONTENT

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/49cbfc4ef2220c778aee8d6123e7c9e7aacaa2dc34f7c8d87f5afe84a17370d5.jpg)


## STRAPI: MANAGING CONTENT

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/76306fcbb78455a469c773b3d3b77fd06aeb73f9eb3fd486bf258d2504241645.jpg)


## STRAPI: USING THE REST API

• For each resource, Strapi automaticallygeneratesREST endpoints 

<table><tr><td>Method</td><td>URL</td><td>Description</td></tr><tr><td>GET</td><td>/api/:pluralApiId</td><td>Get list of entries</td></tr><tr><td>POST</td><td>/api/:pluralApiId</td><td>Create entry</td></tr><tr><td>GET</td><td>/api/:pluralApiId/:resourceId</td><td>Get a specific entry</td></tr><tr><td>PUT</td><td>/api/:pluralApiId/:resourceId</td><td>Update a specific entry</td></tr><tr><td>DELETE</td><td>/api/:pluralApiId/:resourceId</td><td>Delete a specific entry</td></tr></table>

• E.g.: GET /api/courses or DELETE /api/professors/2 

## STRAPI: AUTHORIZING USERS

## • The Strapi UI allows us to create authorizationtokens

• Settings > API Tokens > Create 

• With each token, can specify a name, a duration, and read/write permissions for each resource 

• Users will need to pass the token in the Authorizationheaderwhen using the API (unless we specify thatan endpoint can be accessed withoutauthorization) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/846d0eca9046f9fad70773615bf27419ffe94c1cf69e11388e616c70742f0eeb.jpg)


## STRAPI: AUTHORIZING USERS

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/a2ec23333f6de68971eef64f6eccb4ff11830dc37d041b505bdf11b368cbc2d6.jpg)


## STRAPI: USING THE REST API

```txt
GET http://localhost:1337/api/professors
Authorization: Bearer 97060c911...e12 
```

```json
{
    "data": [
    {
    "id": 1,
    "attributes": {
    "firstName": "Luigi Libero Lucio",
    "lastName": "Starace",
    "email": "luigiliberolucio.starace@unina.it",
    "createdAt": "2023-12-29T07:19:19.746Z",
    "updatedAt": "2023-12-29T07:25:16.666Z",
    "publishedAt": "2023-12-29T07:20:35.307Z"
    }
    },
    ...
} 
```

## STRAPI: USING THE REST API

GET http://localhost:1337/api/professors/2 Authorization: Bearer 97060c911...e12 

```json
{
    "data": {
    "id": 2,
    "attributes": {
    "firstName": "Harold",
    "lastName": "Abelson",
    "email": null,
    "createdAt": "2023-12-29T07:24:16.695Z",
    "updatedAt": "2023-12-29T07:24:17.915Z",
    "publishedAt": "2023-12-29T07:24:17.913Z"
    }
},
"meta": {}
} 
```

## STRAPI: USING THE REST API

```json
POST http://localhost:1337/api/professors
Authorization: Bearer 97060c911...e12
Content-Type: application/json
{
    "data": {
    "firstName": "Anders",
    "lastName": "Hejlsberg",
    "courses": [3, 4]
    }
}

{
    "data": {
    "id": 7,
    "attributes": {
    "firstName": "Anders",
    "lastName": "Hejlsberg",
    "email": null,
    "createdAt": "2023-12-29T08:16:53.132Z",
    "updatedAt": "2023-12-29T08:16:53.132Z",
    "publishedAt": "2023-12-29T08:16:53.126Z"
    }
},
"meta": {}
} 
```

## STRAPI: REST API PARAMETERS

• Strapi endpoints support a numberof Query String parametersto filter, sort, paginateresults, and to select fields and populaterelations 

<table><tr><td>Parameter</td><td>Description</td></tr><tr><td>populate</td><td>Controls which linked resources should be included in the results</td></tr><tr><td>fields</td><td>Selects which fields to include in the result, and in which order</td></tr><tr><td>filters</td><td>Can be used to define custom queries and filter data</td></tr><tr><td>sort</td><td>Controls how the results are sorted</td></tr><tr><td>pagination</td><td>Can be used to control result pagination</td></tr></table>

## STRAPI: POPULATING LINKED RESOURCES

GET http://localhost:1337/api/professors?populate=courses Authorization: Bearer 97060c911...e12 

```json
{"data": [{
    "id": 1,
    "attributes": {
    "firstName": "Luigi Libero Lucio",
    "lastName": "Starace",
    "courses": {
    "data": [{
    "id": 1,
    "attributes": {
    "title": "Web Technologies",
    "credits": 6
    }
    } 
```

```json
{"data": [{
    "id": 1,
    "attributes": {
    "lastName": "Starace",
    "firstName": "Luigi Libero Lucio"
    }
}, { 
    "id": 2,
    "attributes": {
    "lastName": "Abelson",
    "firstName": "Harold"
    }
}, ... 
```

## STRAPI: CUSTOMIZING RETRIEVED FIELDS

GET http://localhost:1337/api/professors?fields[0]=lastName&fields[1]=firstName Authorization: Bearer 97060c911...e12 

## STRAPI: FILTERS

## The filters parameter has the following synta

## GET /api/:pluralApiId?filters[field][operator]=value

```txt
//get courses where credits = 6
GET /api/courses?filters[credits][$eq]=6
Authorization: Bearer 97060c911...e12

//get courses where credits >= 6 and title contains the string "Web"
GET /api/courses?filters[credits][$gte]=6&filters[title][$contains]=Web
Authorization: Bearer 97060c911...e12

//get professors whose firstName contains (case-insensitive) the string "Luigi"
GET /api/professors?filters[firstName][$containsi]=Luigi
Authorization: Bearer 97060c911...e12 
```

## Look at the docs for an exhaustive list of operators and more exampl

## (AN OVERVIEW OF) GRAPHQL

## SOME ISSUES WITH REST

REST is a practical, widelyused way to expose data from a server In some scenarios, however, the REST approachcan be inefficient: 

## • Over-fetching

• Sometimes we do not needall the fields of a resource 

## • Under-fetching

• Sometimes we needlinked resources, and it might be necessary to perform additionalrequests to fetch them 

## • API changes and evolution

• APIs evolve over time. Thus, theyneedto be versioned, maintaina degree of retro-compatibility, deprecate some functionalityover time, 

## REST: OVER- AND UNDER-FETCHING

• Over-fetching and Under-fetching can bothdeteriorate performance an increase data transfers 

• In an over-fetching scenario, we download data we do not need 

• In an under-fetching scenario, we will needto perform(many) additionalrequests to get all the data we need 

• E.g.: first we get the currentuser, thenwe get its posts, then, for each post, we get its comments, etc… 

## GRAPHQL: A QUERY LANGUAGE FOR APIs

• Developedby Facebook 

• Open source version publishedin 2015 

• Specification available at http://spec.graphql.org 

• Designed to address the need for mor flexibility and efficiency 

• Instead of relying on pre-defined endpoints as in REST, allow users to declaratively specifywhich data the need using queries! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/de25d53f56124d961450af1be650c80b1b33cee1555a49484dca37b940593003.jpg)


## GRAPHQL: ARCHITECTURE

GraphQLServer 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/9acad211a355dda1363cb6639e004d3cfd923bc8d4955fb4d605bd46daa57f68.jpg)


Data 

## STRAPI WITH GRAPHQL: EXAMPLE

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-17/967c405c-d84f-4375-87e9-a1a2754e741f/de18c10516c801810a1c9e521ae2aebb97f2fbdba8e4e7d9d8f4fb04ff9923b6.jpg)


@luigi ➜ D/O/T/W/2/e/1/strapi/project-name $ npm install @strapi/plugin-graphql 

## STRAPI WITH GRAPHQL: EXAMPLE

• After restartingStrapi, a GraphQLPlayground will be available at http://localhost:1337/graph 

• In the web technologies course we won’tsee the GraphQLspecification in detail 

• Let’s just grasp the basics with a few examples 

## STRAPI WITH GRAPHQL: EXAMPLES

• Suppose we needto display onlythe last name of each professor 

• Wemight writethe following GraphQ query 

```txt
query {
    professors {
    data {
    attributes {
    lastName
    }
    }
    }
} 
```

```json
{
    "data": {
    "professors": {
    "data": [{
    "attributes": {
    "lastName": "Starace"
    }
    }, {
    "attributes": {
    "lastName": "Abelson"
    }
    }]
    }
} 
```

## STRAPI WITH GRAPHQL: EXAMPLES

• Suppose we needto display only the last name of each professor and the title of theircourses 

```snap
query {
    professors {
    lastName,
    courses {
    title
    }
    }
}

{
    "data": {
    "professors": [
    { "lastName": "Starace",
    "courses": [
    { "title": "Web Technologies" }
    ]
    }
    ]
} 
```

## STRAPI WITH GRAPHQL: EXAMPLES

SELECT title, credits FROM courses WHERE credits >= 6 AND (title CONTAINS «Web» OR title CONTAINS «TypeScript») 

```txt
query {
    courses(filters: {
    credits: { gte: 6},
    or: [{title: {containsi: "Web"}}, {title: {containsi:"TypeScript"}}]
    }) {
    data {
    attributes {
    title, credits
    }
    }
    }
} 
```

# AUTOMATIC GENERATION OF STATIC WEBSITES

## SOMETIMES CMS CAN BE INEFFICIENT

• Sometimes using a full CMS for a website might be overkil 

• In some scenarios, data does not change thatoften 

• Think of a restaurantthatupdates the menu on its website ~ once a month 

• For an entiremonth, each page load will cause a query on the database, which will retrievethe same list of menu entries, and thenthe CMS will display the same contentto users 

• A CMS might be wasting computationcycles (i.e., money, and $\mathbf { \hat { C } 0 } _ { 2 } ! )$ to rende the same pages over and over agai 

• Caching mechanisms exist, but still there’ssome overhead and som computing required 

• CMS needto be keptup to date, whichintroducessome overhead 

## AUTOMATIC STATIC WEBSITE GENERATION

In some scenarios, having a CMS (or a custom web app) render the we pages dynamicallymight be quiteinefficientand wasteful. 

A more efficient approachwouldbe to: 

1. Renderthe web pages onlyonce, whensome changes in the data occur 

2. Serve the compiled(static) web pages to users (which is way more efficient thanrendering these pages dynamically!) 

This approachis referredto as AutomaticStatic Website Generatio 

## AUTOMATIC STATIC WEBSITE GENERATION

One approachto address these issues is to generate static websites automatically 

• Hugo (writtenin Go, used for https://luistar.github.i) 

• Gatsby (generate static websites using React) 

• Jekyll (based on Ruby, used for https://fair-resilient-ai.github.io) 

• Pelican (based on Python) 

• Zola (based on Rust) 

• Manymore are listed here 

## AUTOMATIC STATIC WEBSITE GENERATION

Content 

Templates 

Static Website Generato build 

Static Website 

styles style.css img pic.jpg scripts script.js index.html section article.html project.html 

deploy 

Web Server 

Web Browsers 

## ATTENZIONE

• Per quanto riguarda il progetto, si sottolinea ch 

• La traccia del progetto vieta esplicitamente l’utilizzo di CMS 

• È ammesso, invece, l’utilizzo di GraphQL. 

## DISCLAIMER: COURSE CONTENTS

## • You are notrequiredto learn:

• How to use WordPress, Strapi or any otherCMS 

• The GraphQLspecification, mutations, howto setup a GraphQLserver, or how to writequeries 

• How to use Hugo or otherstatic website generators 

## • You are requiredto learn:

• Whata CMS is and whata CMS can do 

• Whattraditional, headless, and decoupledCMSs are 

• Pros and cons of using a CMS 

• Scenarios in which REST is inefficient, and whatGraphQLis 

• Whatstatic website generatorsare, and whencan theybe used 

## REFERENCES

## • Definition of CM

MDN web docs https://developer.mozilla.org/en-US/docs/Glossary/CMS 

## • Whatis Headless CMS?

Amazon Web Services docs https://aws.amazon.com/what-is/headless-cms/ 

## • The Fullstack Tutorial for GraphQ

Free and open-source tutorial available at https://www.howtographql.co Relevantparts: GraphQLFundamentals (Introduction, GraphQLis the betterREST, Core Concepts, Big Picture (Architecture 

## • Whatis a static site generator?

Article in the CloudflareLearning Resources Available at https://www.cloudflare.com/learning/performance/static -site-generator/and archivedhere 