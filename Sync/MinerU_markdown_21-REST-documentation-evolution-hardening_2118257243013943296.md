## FROM WORKING APIs TO PRODUCTION-READY APIs

Luigi Libero Lucio Starace, PhD 

luigiliberolucio.starace@unina. 

https://luistar.github.io; https://squids.unina.i 

https://www.docenti.unina.it/luigiliberolucio.stara 

## TODAY’S GOAL

• A backend is not finished as soon as the endpoints wor 

• A backend becomes mature whenit can evolve, survive clients, resist abuse, and be operatedsafely. 

• Some questions we should be able to answer: 

• How do we documentan API? 

• How do we change the API withoutbreaking existing clients? 

• How do we protectresources from unauthorizedaccess? 

• How do we limit abuse and excessive traffic? 

• How do we observewhatis happening in production 

• How do we safely retireold functionality? 

## OPENAPI: DESCRIBING A REST API

• OpenAPI(formerlySwagger) is an open, formal standard to describe HTTP APIs 

• Why? 

• Standardization: ensures consistent documentationpractices 

• Documentation: can be used to automatically generate comprehensivedocs 

• Code generation: Allows for automatic generation of client libraries and server stubs 

• Machine and human-readable: enables automateddiscovery and more 

• Most broadly adopted industry standa 

![image|700x701](https://cdn-mineru.openxlab.org.cn/result/2026-11-05/ec33f2dc-73ff-45b4-a0cf-b1f173a14774/945189b19923487e50791ef6e949a4d9d4d70502f81f2580491c1d1a83228212.jpg)


## THE OPENAPI SPECIFICATION

## • OpenAPIDescriptions are writtenas structuredtext documents

• Each documentrepresentsa JSON object, in JSON or YAML format 

• These specification files describe version of the OpenAPIspecification (openapi), the API (info) and the endpoints (paths) 

```txt
# YAML format
openapi: 3.1.0
info:
    title: A minimal specification
    version: 0.0.1
paths: {} # No endpoints defined

// JSON format
{
    "openapi": "3.1.0",
    "info": {
    "title": "A minimal specification",
    "version": "0.0.1"
},
"paths": {} // No endpoints defined
} 
```

## THE OPENAPI SPECIFICATION: PATHS

• The API Endpoints are called Paths in the OpenAPIspecification 

## • Path objects allow to specify a sequence of endpoints

• For each endpoint, its supportedmethods 

• For each method, 

• Expected input parameters(if any) (e.g.: path parameters, headers, etc…) 

• Requestbody (if any) 

• Possible responses 

• And more! 

## THE OPENAPI SPECIFICATION: PATHS

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-05/ec33f2dc-73ff-45b4-a0cf-b1f173a14774/0434b34c5b37bdd4e5c498d3b89814639ba99c7692b83b8954695e6c834262b0.jpg)



Image from https://learn.openapis.org/specification/path


## PATH EXAMPLE

• /authendpoint, POST method 

• Expects RequestBody containinga JSON object with type {usr: string, pwd: string} 

• Returns200 OK on success, 401 Unauthorizedwhencredentials are invalid 

```yaml
/auth:
    post:
    description: Authenticate user
    produces:
    - application/json
requestBody:
    description: user to authenticate
    required: true
    content:
    application/json:
    schema:
    type: object
    properties:
    usr:
    type: string
    example: Kyle
    pwd:
    type: string
    example: p4ssw0rd
responses:
200:
description: User authenticated
401:
description: Invalid credentials 
```

## WORKING WITH OPENAPI SPECIFICATIONS

• Writing an OpenAPIspecification for an API is quitea lot of work 

• Whatcan we do with an OpenAPIspecification? 

```yaml
openapi: 3.1.0
info:
    title: My API
    version: 1.0.0
paths:
    /auth:
    post:
    # ...
    /todos:
    get:
    # ...
    post:
    # ... 
```

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-05/ec33f2dc-73ff-45b4-a0cf-b1f173a14774/b1ad27699c11f2ce09b307861729d7d273be3342a8fe00688405412439533ccb.jpg)



Generate Cod Server stubs, client SDKs , tests


## OPENAPI: OPEN SOURCE TOOLS

• OpenAPIis supportedby a numberof mature, open-source tools 

• Some widelyused open-source tools are reportedas follows: 

• Swagger Editor: https://swagger.io/tools/swagger-editor/ 

• Swagger Codegen: https://swagger.io/tools/swagger-codegen/ 

• Swagger UI: https://swagger.io/tools/swagger-ui/ 

• A free alternative is https://openapi-generator.tech 

## OPENAPI: SWAGGER EDITOR

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-05/ec33f2dc-73ff-45b4-a0cf-b1f173a14774/e2bbf45c4d68cf77de5c0225a16eb36cda3a5b1451f55fda92bdadc9be088394.jpg)



Specification



Documentation(Swagger UI)


## OPENAPI: CODEGEN

• From the editor toolbar, we can also generate Server and Client cod 

• Server-side code generation can obviouslyonly providestubs 

• Supportedlanguages/frameworks include: ASP.NET, Go, Java, JaxRS , Micronaut, Kotlin, Node.js, Python (Flask), Scala, Spring. 

• Client-side code generation is a veryhandyway to make SDKs for our APIs available in tens of differentlanguages 

• Supportedlanguages include: C#, Dart, Go, Java, JavaScript, Kotlin, PHP, Python, R, Ruby, Scala, Swift, TypeScript 

## OPENAPI-DRIVEN DEVELOPMENT

• Often, developers start working on an API by defining its specification beforewriting any actual code 

• This approachis also referredto as OpenAPI-drivendevelopment 

• This way, theycan exploit code generation capabilities to the fullest 

• The approachalso promotesindependencebetweenthe different teams involvedin a project (front-end, back-end, QA). The API definition keeps all these stakeholders aligned 

## API EVOLUTION

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-05/ec33f2dc-73ff-45b4-a0cf-b1f173a14774/6827966bc1abacace19cea57a5430d8368f3c4da08ebd50e3814e8e511a345a6.jpg)


## THE API IS A CONTRACT

• When we expose an API, we create a contrac 

• The contract includes: 

• URL paths and HTTP method 

• Request body forma 

• Response body forma 

• Status codes 

• Authentication requirements and Authorization ru 

• Error forma 

• Performance expectation 

• Even if we do not write the contract down, clients will depend on 

## API EVOLUTION: WHY IT HAPPENS

• APIs, like any othermeaningfulsoftware, will evolve over tim 

• Some change causes may be: 

• Business rule change 

• Frontendrequirementschange 

• Mobile apps neednew fields 

• Old data model becomes insufficient 

• Performance issues appear 

• Security requirementschange 

• Integrationswith thirdparties evolve 

## SAFE VS BREAKING CHANGES

• Some changes are «safe» with respect to the API contract • These change do not affect existing clients 

• … whileothersare not safe 

• These changes can cause existing clients to stop working with the new A 

• They are referredto as (potentially) breaking changes 

## SAFE VS BREAKING CHANGES: EXAMPLES

## USUALLY SAFE

• Add a new endpoin 

• Add a new optional req. field 

• Add a new optional res. fiel 

• Add a new filter param. with default 

• Improve internal implementatio (e.g.: refactoring) without alterin behaviou 

## POTENTIALLY BREAKING

• Renamea field 

• Removea field 

• Change a field type 

• Change status codes 

• Change errorresponse format 

• Change semantic behaviourof existing endpoin 

• Change AuthN/Z requirement 

## SAFE CHANGE: EXAMPLE

• Adding a new field to a response is typically safe 

• Clients should ignoreunknownfields 

```json
{
    "id": 1,
    "title": "Prepare lecture",
    "completed": false
} 
```

## BREAKING CHANGE: EXAMPLE

• New requirement: we need to track task status with finer granularit • «TODO», «IN-PROGRESS», «DONE 

```json
{
    "id": 1,
    "title": "Prepare lecture",
    "completed": false
} 
```

## EVOLUTIONARY STRATEGIES

• Wecannot restrict our API to only safe changes 

• At some points, breaking changes may be necessary 

• Whenretro-compatibilityis broken, we needan evolutionar strategy 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-05/ec33f2dc-73ff-45b4-a0cf-b1f173a14774/078dc95ddad028eec20e398ff552ee0f3e2e9d3b9d4c35a4ee026ad51aa72453.jpg)


## API VERSIONING: BASIC IDEA

• Whenwe make breaking changes, we may wantto keep botholderand newerversions of our API up (at least for some time) 

• Weshould allow clients to use differentversions of our API 

• Common strategies include 

## • URI Versioning

• /api/v1/tasks 

• /api/v2/tasks 

• Allowing clients to specify the version theywantusing requestheaders • X-API-Version: 2 

• Accept: application/vnd.academy.tasks.v2+json 

## URI VERSIONING

• GET /api/v1/tasks/1 

• GET /api/v2/tasks/1 

• Pros: 

• Easy to understand and tes 

• Easy to documen 

• Easy to route in most framework 

## • Disadvantages

• Can create some duplications in controllers/router 

## DJANGO NINJA EXAMPLE

```python
# api_v1.py
from ninja import NinjaAPI

api = NinjaAPI(version="1.0.0")

@api.get("/tasks/{task_id}")
def get_task(request, task_id: int):
    return {
    "id": task_id,
    "title": "Prepare lecture",
    "completed": False,
    }

from django.contrib import admin
from django.urls import path
from tasks.api_v1 import api as api_v1
from tasks.api_v2 import api as api_v2

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api_v1.urls),
    path("api/v2/", api_v2.urls)
]

# api_v2.py
from ninja import NinjaAPI

api = NinjaAPI(version="2.0.0")

@api.get("/tasks/{task_id}")
def get_task(request, task_id: int):
    return {
    "id": task_id,
    "title": "Prepare lecture",
    "status": "OPEN",
    }
Docs will be generated in separated directories:
• http://localhost:8000/api/v1/docs
• http://localhost:8000/api/v2/docs 
```

## SPRING BOOT EXAMPLE

```java
@RestController
@RequestMapping("/api/v1/tasks")
public class TaskControllerV1 {

    @GetMapping/{id}")
    public TaskResponseV1 getTask(@PathVariable Long id) {
    return new TaskResponseV1(
    id,
    "Prepare lecture",
    false
    );
    }
}

public record TaskResponseV1(
    Long id,
    String title,
    boolean completed
) {}

@RestController
@RequestMapping("/api/v2/tasks")
public class TaskControllerV2 {

    @GetMapping/{id}")
    public TaskResponseV2 getTask(@PathVariable Long id) {
    return new TaskResponseV2(
    id,
    "Prepare lecture",
    "OPEN"
    );
    }
}

public record TaskResponseV2(
    Long id,
    String title,
    String status
) {} 
```

## RULES TO VERSION BY

• Do not create a new version for everysmall change 

• Use versioningonly whenthereis a breaking change 

• Maintainingmultiple versions at the same time is a huge effort! 

• Good rule: 

• Add withoutversioning, removeor redefinewith versioning. 

## DEPRECATION AND SUNSET

• Versioning is not enough 

• Wealso needlifecycle communication 

• Generally, we do not wantto support an old API forever 

• Typical lifecycle includes: 

## Active

• Recommended version 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-05/ec33f2dc-73ff-45b4-a0cf-b1f173a14774/97cb6d13ab291695dbb65e347cd8334cbbb718a783bda584396b4cfb31995d2e.jpg)


## Deprecated

• Still works, but clients should migrate to active version 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-05/ec33f2dc-73ff-45b4-a0cf-b1f173a14774/cd47c49de186f9672de8fef6273e5b73bee720a3e885b112d9f9da711741d0f5.jpg)


## Sunset

• Still works, but removal date is announced 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-05/ec33f2dc-73ff-45b4-a0cf-b1f173a14774/ad6818fc362fa8ddc4fdb808a6780d5eecc6d027d68820d160599b2a2671794a.jpg)


## Removed

API version no longer available 

## DEPRECATION AND SUNSET

• The importantidea is to not break client silently 

• You should give themfair warning beforea breaking change occurs 

• A deprecatedendpoint may continue working as intended, butmay returnadditionalwarning headers 

• E.g.: Deprecation, Sunset, Link 


HTTP response with warning headers


```txt
HTTP/1.1 200 OK
Deprecation: true
Sunset: Wed, 31 Dec 2026 23:59:59 GMT
Link: </docs/migrate-v1-to-v2>; rel="deprecation"
Content-Type: application/json
{ "foo": "bar" } 
```

## ADDING WARNING HEADERS: SPRING BOOT

```txt
@GetMapping("/api/v1/tasks/{id}")
public ResponseEntity<TaskResponseV1> getTaskV1(@PathVariable Long id) {
    TaskResponseV1 body = new TaskResponseV1(
    id,
    "Prepare lecture",
    false
    );
    return ResponseEntity.ok()
    .header("Deprecation", "true")
    .header("Sunset", "Wed, 31 Dec 2026 23:59:59 GMT")
    .header("Link", "</docs/migrate-v1-to-v2>; rel=\"deprecation\"")
    .body(body);
} 
```

## ADDING WARNING HEADERS: DJANGO NINJA

```python
@api.get("/tasks/{task_id}")
def get_task_v1(request: HttpRequest, task_id: int):
    response = api.create_response(
    request,
    {
    "id": task_id,
    "title": "Prepare lecture",
    "completed": False,
    },
)
response["Deprecation"] = "true"
response["Sunset"] = "Wed, 31 Dec 2026 23:59:59 GMT"
response["Link"] = '</docs/migrate-v1-to-v2>; rel="deprecation'"
return response 
```

## API SECURITY AND HARDENING

## API SECURITY RISKS

• The OWASP API Security Top 10 includes: 

1. Broken Object Level Authorizatio 

2. Broken Authenticatio 

3. Broken Object Property Level Authorizatio 

4. Unrestricted Resource Consumptio 

5. Broken Function Level Authorizatio 

6. Unrestricted Access to Sensitive Business Flows 

7. Server Side Request Forger 

8. Security Misconfiguratio 

9. Improper Inventory Manageme 

10. Unsafe consumption of APIs 

# BROKEN OBJECT LEVEL AUTHORIZATION

• Dangerous endpoint: GET /api/tasks/42 

• Client may be authenticated, buttask 42 may not belongto them! • Developers oftenforget to properlymanage object-level authorization, and over-rely on authenticatio 

```python
public TaskResponse getMyTaskById(Long userId, Long taskId) {
    Task task = taskRepository.findByIdAndOwnerId(taskId, userId)
    ._orElseThrow(() -> new ResponseStateException(
    HttpStatus.NOT_FOUND, "Task not found"
    ));
    return toResponse(task);
}

@api.get("/tasks/{task_id}", response={200: TaskOut, 404: ErrorOut}, auth=jwt_auth)
def get_task(request, task_id: int):
    try:
    task = Task.objects.prefetch_related("tags").get(
    id=task_id,
    owner=request.auth,
    )
except Task.DoesNotExist:
    return 404, {"error": "Task not found"}
return task_to_out(task) 
```

## BROKEN AUTHENTICATION

## • Impact:

• Attackers can gain control of otheruser’s accounts, accessing personal data and performingsensitive operations 

• An API is vulnerableif: 

• JWT secret key is exposed or predictable 

• Permits weak passwords 

• Allows users to change email address/password or do sensitive operations withoutrequiringpassword confirmation 

• Doesn’tvalidate tokens correctly(e.g.: ignores expirationdate) 

• Allows attackers to performbrute force attacks withoutlockout mechanisms 

## BROKEN OBJECT PROPERTY LEVEL AUTHZ

## • Impact:

• Unauthorizedaccess to private/sensitive object propertiesmay result in unwanteddata disclosure 

• An API is vulnerableif: 

• Exposes propertiesof an object that are considered sensitive 

• Allows users to change/add/delete the vallue of a sensitive object propert 

• Typically associated with returningmodels directlywithoutusing DTOs/Schemas 

## UNRESTRICTED RESOURCE CONSUMPTION

• APIs often don’t limit client interactions or resource consumption 

• This can be exploitedby attackers for DoS attacks or to increase operationalcosts 

• An API is vulnerableif at least one of the following limits is set inappropriately: 

• Execution timeout 

• Rate limit (how many requests per client per unit of tim 

• Maximum allocable memor 

• Maximum number of processe 

• Maximum upload file siz 

• Number of records per page to return in a single request -response 

• Third-party service providers' spending lim 

## RATE LIMITING

• Rate limiting controls how many requests a client can mak 

• It helps with: 

• Abuse preventio 

• Brute-force reduction 

• Cost control 

• Fair usage 

• Protecting expensive endpoint 

• Reducing accidental overloa 

## • Enforce a maximum number of requests per user per feature per unit time

## EXPRESS 5 RATE LIMITING

## https://www.npmjs.com/package/express-rate-limit

```javascript
import { rateLimit } from 'express-rate-limit'

const limiter = rateLimit({
    windowMs: 60 * 1000, // 1 minute
    limit: 10, // Limit each IP to 100 requests per `window` (here, per 15 minutes).
    standardHeaders: 'draft-8',
    legacyHeaders: false, // Disable the `X-RateLimit-*` headers.
    ipv6Subnet: 56,
})

// Apply the rate limiting middleware to all requests.
app.use(limiter) 
```

## DJANGO NINJA THROTTLING

```python
from ninja import NinjaAPI
from ninja.throttling import AnonRateThrottle, AuthRateThrottle

api = NinjaAPI(
    title="Namirial Academy Tasks API",
    version="2.0.0",
    description="REST API for users, tasks, tags, and JWT authentication.",
    throttle=[
    AnonRateThrottle("1/s"),
    AuthRateThrottle("10/s"),
    ]
) 
```

## • Django Ninja supports global, router-level and method-level throttling: https://django-ninja.dev/guides/throttling

## DJANGO NINJA THROTTLING

## • Example with operation-level throttling

![image](https://cdn-mineru.openxlab.org.cn/result/2026-11-05/ec33f2dc-73ff-45b4-a0cf-b1f173a14774/37e7ddd453641f9fcbf677cf9d4ae6b02b7d747fefbaf7236d65178c3f911800.jpg)


## SPRING BOOT RATE LIMITING

• If you’re interestedin implementinga rate limiting mechanism in Spring Boot you may check out libraries like Bucket4j 

```xml
<!-- Bucket4j for java 17+ -->
<dependency>
    <groupId>com.bucket4j</groupId>
    <artifactId>bucket4j_jdk17-core</artifactId>
    <version>8.18.0</version>
</dependency> 
```

## SPRING BOOT RATE LIMITING

```java
@Service
public class LoginRateLimiter {

    private final Map<String, Bucket> buckets = new ConcurrentHashMap◇();

    public boolean tryConsume(String key) {
    Bucket bucket = buckets.computeIfAbsent(key, this::newBucket);
    return bucket.tryConsume(1);
    }

    private Bucket newBucket(String key) {
    Bandwidth limit = Bandwidth.classic(
    5,
    Refill.greedy(5, Duration.ofMinutes(1));
    );
    return Bucket.builder().addLimit(limit).build();
    }
} 
```

## SPRING BOOT RATE LIMITING

```txt
@PostMapping("/login")
public ResponseEntity<?> login(@RequestBody AuthRequest request, HttpServletRequest requests) {
    //rate limiting enforcement
    String key =gebClientIp (httpRequest) + ":" + request.username();

    if (!loginRateLimiter.tryConsume(key)) {
    return ResponseEntity
    .status (HttpStatus.TOO_MANY_REQUESTS)
    .body (Map.of(
    "error", "RATE_LIMITED",
    "message", "Too many login attempts"
    ));
    }
    return ResponseEntity.ok (authService.login(request));
}

Response Timeline >> 429 Too Many Requests 6ms 60B Clear Timeline

429 POST http://localhost:8080/api/auth/login 10 minutes ago
429 POST http://localhost:8080/api/auth/login 10 minutes ago
401 POST http://localhost:8080/api/auth/login 10 minutes ago
401 POST http://localhost:8080/api/auth/login 10 minutes ago
401 POST http://localhost:8080/api/auth/login 10 minutes ago
401 POST http://localhost:8080/api/auth/login 10 minutes ago 
```

## BROKEN FUNCTION LEVEL AUTHORIZATION

## • Authorizationflaws thatallow attackers to access unauthorized functionalit

• Example: 

• Onlystaff membersshould be able to DELETE /api/tags/{id}, butwe implementthis check incorrectly(or we don’tat all!) 

## UNRESTRICTED ACCESS TO SENSITIVE FLOWS

• APIs may expose sensitive business flows 

• Common examples of sensitive business: 

• Purchasing a product flow - an attacker can buy all the stock of a high-demand item at once and resell for a higher price (scalping 

• Creating a comment/post flow - an attacker can spam the system 

• Making a reservation - an attacker can reserve all the available time slots an prevent other users from using the syste 

• Mitigation: Restrict access to sensitive flows 

• Step 1: Identify sensitive business flows 

• Step 2: Engineering solutions: Device fingerprinting; Human-detection; Detecting non-human usage patterns; Blocking IP addresses 

## SERVER-SIDE REQUEST FORGERY

• If an endpoint makes a requestto some remote URI providedin requests by client, the URI should be properlyvalidated 

• Otherwise, attackers can force the API to make requests to unexpected destinations 

• This may result in exposure of sensitive information 

```txt
POST /api/profile/upload_picture
{
    "picture_url": "http://example.com/profile_pic.jpg"
}
{
    "picture_url": "localhost:8080"
} 
```

Based on the response time, th attacker can figure out whether th port is open or not 

## SECURITY MISCONFIGURATIONS

• API frameworks typically contain complex configurations, meant make them more customizable and support many use case 

• Software and DevOps engineers can miss these configurations, or don follow security best practices when it comes to configuration, openi the door for different types of attack 

• Examples: 

• API deployed in debug/dev mode → exposure of stack traces 

• TLS not configured 

• Latest security patches missing 

## ERROR RESPONSES

## • Errors are part of the API Contract

## • Mature APIs returnpredictableand consistent errors

```json
{
    "error": "VALIDATION_ERROR",
    "message": "Title must not be blank",
    "details": {
    "field": "title"
    }
} 
```

## • Avoid leaking internals

```json
{
    "error": "NullPointerException at TaskService.java:47"
} 
```

## IMPROPER INVENTORY MANAGEMENT

• Sometimes, an organization does not clearly know which API endpoints, versions, envs, and data flows are currently expose 

• This becomes dangerous when old/forgotten APIs remain reachabl 

```txt
/api/v1/admin/users
/api/test/tasks
/api/debug/tokens
/api/v0/legacy-login 
```

• Attackers often look for forgotten endpoints because they may ha weaker authentication, missing authorization checks, or kno vulnerabilities. 

## UNSAFE CONSUMPTION OF APIs

• Oftendevelopers tendto trust data providedby third-party APIs more thanclient-provideddata 

• This is dangerous, because externalservices are outside of our control as well, and should be treatedwith the same suspicion 

• Attackers may compromise trustedthird-party $A P | s$ 

• Send redirects to malicious services 

• Or send malicious payloads in requests (e.g.: SQL Injections)… 

## OBSERVABILITY

• In production, we should be able to (automatically) observethe status of the API 

• Is the application running? 

• Is the database reachable? 

• How many requests are failing? 

• Which endpoints are slow 

• Are users receiving 401, 403, 404, or 500 responses? 

• Are rate limits being triggered 

• Are old API versions still used? 

• Without observability, production problems become guessin 

## OBSERVABILITY IN SPRING BOOT

## • Add the Actuatordependencyto the pom.xm

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency> 
```

## • Add the following line to application.propertiesto expose info and metrics data

```txt
#Actuator config
management.endpoints.web.exposure.include=* 
```

## OBSERVABILITY IN SPRING BOOT

## • You can make a requestto /actuator/health to get status details

```txt
GET http://localhost:8080/actuator/health
Send
Params Body Headers 1
Query
Name Value
Name Value
Bulk Edit
Path ?
{
    "groups": [
    "liveness",
    "readiness"
    ],
    "status": "UP"
} 
```

## • Possible status values: UP, DOWN, OUT_OF_SERVICE; UNKNOW

## OBSERVABILITY IN SPRING BOOT

• You may also get more detailed metrics using the actuator/metrics endpoin 

• The GET returnsa list of available metrics 

• You needto make follow up get requests to /actuator/metrics/{name} to get the correspondingvalues 

<table><tr><td>Name</td><td>Value</td><td></td></tr><tr><td>Name</td><td>Value</td><td></td></tr></table>

## OBSERVABILITY IN SPRING BOOT

• For example, a requestto /actuator/metrics/system.cpu.usage may return 

```jsonl
Response Headers 12 Timeline Tests {} JSON 200 OK 8ms 198B
{
    "availableTags": [],
    "description": "The \"recent cpu usage\" of the system the application is running in",
    "measurements": [
    {
    "statistic": "VALUE",
    "value": 0.13948267002189407
    }
    ],
    "name": "system.cpu.usage"
} 
```

## MINIMAL OBSERVABILITY IN DJANGO NINJA

```groovy
@api.get("/health", auth=None)
def health(request):
    with connection.cursor() as cursor:
    cursor.execute("SELECT 1")
return {
    "status": "ok",
    "database": "ok"
} 
```

## LOGGING

## • Useful logs:

• Authentication failure 

• Authorization failure 

• Rate limit violation 

• Unexpected server error 

• Deprecated API usage 

• Admin actions 

• Data-changing operations 

• External service failures 

## • Avoid logging:

• Passwords 

• Tokens 

• Full Authorization header 

• Sensitive personal data 

• Full request bodies by defaul 

• Logs are operational tools, but they can also become security risk 

## REFERENCES (1/2)

## • The Little Book on REST Services

By Kenneth Lange Freelyavailable at https://www.kennethlange.com/books/The-Little-Book-on-REST-Services.pdf 

## • API design guide

Google Cloud https://cloud.google.com/apis/desig Relevantparts: Resource-orienteddesign, Resource names. 

• REST API Checklist By Kenneth Lange https://kennethlange.com/rest-api-checklist/ 

# • REST API Design Rulebook: Designing Consistent RESTful We Service Interfaces By Mark Massé

## REFERENCES (2/2)

## • OpenAP

Official Website 

https://www.openapis.org 

https://learn.openapis.org/(Recommendedreads from this link: Gettingstarted, Introduction) 

https://spec.openapis.org/oas/v3.1.0 (Full specification for OpenAPI 3.1.0) 

For the Web Technologies course, you needto know whatthe OpenAPIspecification standard is, whyit has beenintroduced, and whatit can be used for. You are notrequiredto learnhowto writeOpenAPIspecification files from scratch. 

## • API Documentation: The Secret to a Great API Developer Experien

Ebook by SmartbearSoftware 

Available at https://swagger.io/resources/ebooks/api-documentation-the-secret-to-a-great-api-developerexperience and archivedhere. 

Interesting read. Notrequiredfor the Web Technologies course, but it can be useful to betterunderstandthe challenges in designing and documentingan API. 

## EXAMPLES WITH DIFFERENT FRAMEWORKS

## • To-do List REST API using JakartaEE (Java)

By Luigi Libero Lucio Starace Includes source code, Dockerfile and instructions. https://github.com/luistar/jakartaee-rest-example 

## • Pizza Shop REST API using Spring (Java)

By Luigi Libero Lucio Starace https://github.com/luistar/rest-service-pizzashop 

## • Quiz REST API using FastAPI (Python)

By MárcioLemos https://github.com/marciovrl/fasta 

！ You are notrequiredto learn JakartaEE, Spring, or FastAPI for the Web Technologies course. It might be educationallyworthwhileto take a look at some web frameworks otherthanExpress. JakartaEE and Spring, for example, use an annotation-based approach. So, feel free to look at the code or tryto runthe abovelinkedREST API, but be awarethat it’s not requiredfor this course. 