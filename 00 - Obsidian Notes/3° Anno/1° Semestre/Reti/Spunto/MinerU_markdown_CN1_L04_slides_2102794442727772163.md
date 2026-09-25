## The Application Layer: HTTP

Lecture 4 

## A<sub>pp</sub>lication La<sub>y</sub>er Web and HTTP

• Until the early 1990s the Internet was used primarily by researchers, academics<sub>,</sub> and universit<sub>y</sub> students 

• To lo<sub>g</sub> in to remote hosts (Telnet)<sub>,</sub> to transfer files (FTP)<sub>,</sub> to receive and send news<sub>,</sub> to r<sub>ece</sub>i<sub>ve</sub> <sub>a</sub>nd <sub>se</sub>nd <sub>e</sub>l<sub>ec</sub>tr<sub>o</sub>ni<sub>c</sub> m<sub>a</sub>il<sub>.</sub> 

• Althou<sub>g</sub>h these a<sub>pp</sub>lications were (and continue to be) extremel<sub>y</sub> useful<sub>,</sub> the Int<sub>e</sub>rn<sub>e</sub>t <sub>w</sub>a<sub>s</sub> <sub>esse</sub>ntiall<sub>y</sub> <sub>u</sub>nkn<sub>ow</sub>n <sub>ou</sub>t<sub>s</sub>id<sub>e</sub> <sub>o</sub>f th<sub>e</sub> a<sub>c</sub>ad<sub>e</sub>mi<sub>c</sub> and r<sub>ese</sub>ar<sub>c</sub>h comm<sub>u</sub>nities<sub>.</sub> 

• In the early 1990s the World Wide Web was the first Internet application that cau<sub>g</sub>ht the <sub>g</sub>eneral <sub>p</sub>ublic<sub>.</sub> 

## A<sub>pp</sub>lication La<sub>y</sub>er Web and HTTP

• The World Wide Web (WWW or sim<sub>p</sub>l<sub>y</sub> Web) is a collection of information such as documents<sub>,</sub> im<sub>ages,</sub> <sub>v</sub>id<sub>eo,</sub> <sub>au</sub>di<sub>o,</sub> <sub>e</sub>t<sub>c.</sub> th<sub>a</sub>t <sub>ca</sub>n b<sub>e</sub> <sub>accesse</sub>d <sub>ove</sub>r th<sub>e</sub> Int<sub>e</sub>rn<sub>e</sub>t <sub>acco</sub>rdin<sub>g</sub> t<sub>o</sub> <sub>a</sub> <sub>spec</sub>ifi<sub>c</sub> <sub>p</sub>r<sub>o</sub>t<sub>oco</sub>l called HyperText Transfer Protocol (HTTP). 

• HTTP<sub>-</sub>based comm<sub>u</sub>nication is t<sub>yp</sub>icall<sub>y</sub> client-server<sub>:</sub> 

• A client program that translates users’ requests into HTTP messages. This is implemented into the web browsers (Chrome<sub>,</sub> Firefox<sub>,</sub> Ed<sub>g</sub>e<sub>,</sub> Safari<sub>,</sub> etc.). 

• A server program that executes the HTTP request and returns a HTTP response. 

• HTTP m<sub>a</sub>inl<sub>y</sub> d<sub>e</sub>fin<sub>es:</sub> 

• the structure of messages 

• how client and server exchange such messages. 

• The Web and its protocols serve as a platform for web-based applications such as YouTube, Webbased e-mail (e.<sub>g</sub>.<sub>,</sub> Gmail)<sub>,</sub> and most mobile Internet a<sub>pp</sub>lications<sub>,</sub> includin<sub>g</sub> Social Networks. 

## A<sub>pp</sub>lication La<sub>y</sub>er URL

• The information on the web are called resources (or objects) and are identified b<sub>y</sub> a Uniform Resource Locator (URL) which is a strin<sub>g</sub> com<sub>p</sub>osed as follows: 

[<sub>p</sub>rotocol]://[usrinfo@][host][:<sub>p</sub>ort][/<sub>p</sub>ath][?<sub>q</sub>uer<sub>y</sub>][#fra<sub>g</sub>ment] 

## • Wh<sub>ere:</sub>

• [<sub>p</sub>rotocol] is the protocol to use while accessin<sub>g</sub> the resource (HTTP<sub>,</sub> HTTPS<sub>,</sub> FTP<sub>,</sub> etc.). 

• [usrinfo] (o<sub>p</sub>tional) are user’s information such as username and <sub>p</sub>assword followed b<sub>y</sub> a @ (e.g.<sub>,</sub> username:password@). This is mostly deprecated due to security issues. 

• [host] is the name or the IP address of the server. 

• [<sub>p</sub>ort] (o<sub>p</sub>tional) is the port to use (often inferred from the <sub>p</sub>rotocol). 

• [<sub>p</sub>ath] is the path of the resource within the server (e.<sub>g</sub>.<sub>,</sub> /<sub>p</sub>ath/to/resource). 

• [query] is preceded by the ? and specifies possible requests. 

• [fra<sub>g</sub>ment] <sub>p</sub>receded b<sub>y</sub> the # identifies an element in the resource (e.<sub>g</sub>.<sub>,</sub> a form). 

## A<sub>pp</sub>lication La<sub>y</sub>er URL

• Most Web <sub>p</sub>a<sub>g</sub>es consist of a base HTML (H<sub>yp</sub>erText Marku<sub>p</sub> Lan<sub>g</sub>ua<sub>g</sub>e) file and several references to additional objects (ima<sub>g</sub>es<sub>,</sub> videos<sub>,</sub> Java a<sub>pp</sub>lets<sub>,</sub> etc.). 

• Example: a Web page containing HTML text and five JPEG images has six objects: the base HTML fil<sub>e</sub> <sub>p</sub>l<sub>us</sub> th<sub>e</sub> fi<sub>ve</sub> im<sub>ages.</sub> 

## • An exam<sub>p</sub>le of URL is<sub>:</sub>

htp://www.someSchool.edu/someDepartment/picture1.gif 

• Wh<sub>ere:</sub> 

• htp is the protocol. 

• www.someSchool.edu is the hostname<sub>.</sub> 

• /someDepartment/picture1.gif is the path to the object. 

## A<sub>pp</sub>lication La<sub>y</sub>er URL

## • Real exam<sub>p</sub>le of URL <sub>q</sub>uer<sub>y:</sub>

## ht<sub>ps:</sub>//<sub>e</sub>n<sub>.w</sub>iki<sub>pe</sub>dia<sub>.o</sub>r<sub>g</sub>/<sub>w</sub>/ind<sub>ex.p</sub>h<sub>p</sub>?titl<sub>e=</sub>SSC<sub>_</sub>Na<sub>po</sub>li

## • Where:

• htps is the protocol. 

• en.wikipedia.org is the hostname. 

• /w/index.php is the path to the page. 

• ?title=SSC_Napoli is the query. 

• In this case<sub>,</sub> it is the same as askin<sub>g</sub> for the <sub>p</sub>a<sub>g</sub>e<sub>:</sub> ht<sub>ps:</sub>//<sub>e</sub>n<sub>.w</sub>iki<sub>pe</sub>dia<sub>.o</sub>r<sub>g</sub>/<sub>w</sub>iki/SSC<sub>_</sub>Na<sub>po</sub>li 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/8a02ed49302d2bc67844ae9e319902ed1e23d377b4232c20663d9b3a331b82d5.jpg)



<sub>e</sub>n<sub>.w</sub>iki<sub>pe</sub>di<sub>a.o</sub>r<sub>g</sub>/<sub>w</sub>iki/SSC<sub>_</sub>N<sub>apo</sub>li


## A<sub>pp</sub>lication La<sub>y</sub>er HTTP

• HTTP defines how Web clients request objects (e.g., Web <sub>p</sub>a<sub>g</sub>es) from Web servers and how servers transfer them to <sub>c</sub>li<sub>e</sub>nt<sub>s.</sub> 

• When a user requests an object (for example, a Web page b<sub>y</sub> clickin<sub>g</sub> on a h<sub>yp</sub>erlink)<sub>,</sub> the browser sends HTTP request messages for the objects in the page to the server. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/e6e3c3600395583da55c2fc085f04a29bcef38357b5e621f0892e2af3614f5e8.jpg)


• The server receives the re<sub>q</sub>uests and res<sub>p</sub>onds with HTTP response messages that contain the objects. 

• HTTP is continuously evolving to match the re<sub>q</sub>uirements (reliabilit<sub>y</sub> vs. <sub>p</sub>erformance) of modern networkin<sub>g</sub>. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/cfe2ceef2aac6e3510f9803b4efafe6948880a6ebfbbf9e18ff704f881d2466b.jpg)


## A<sub>pp</sub>lication La<sub>y</sub>er HTTP<sub>:</sub> Trans<sub>p</sub>ort Protocol

• HTTP mainly uses TCP as its underlying transport protocol, but from 2022 (version HTTP/3) it may also use UDP. 

• Around 30% of the overall HTTP trafic is on UDP [Wiki<sub>p</sub>edia<sub>,</sub> 2024]. 

• The HTTP client first initiates a connection with the server<sub>.</sub> Once the <sub>co</sub>nn<sub>ec</sub>ti<sub>o</sub>n i<sub>s</sub> <sub>es</sub>tabli<sub>s</sub>h<sub>e</sub>d<sub>,</sub> th<sub>e</sub> br<sub>owse</sub>r and th<sub>e</sub> <sub>se</sub>r<sub>ve</sub>r <sub>p</sub>r<sub>ocesses</sub> <sub>w</sub>ill communicate throu<sub>g</sub>h their socket interfaces<sub>.</sub> 

• The client sends HTTP re<sub>q</sub>uest messa<sub>g</sub>es into its socket interface and receives HTTP res<sub>p</sub>onse messa<sub>g</sub>es from its socket interface<sub>.</sub> Similarl<sub>y,</sub> the HTTP server r<sub>ece</sub>i<sub>ves</sub> r<sub>eques</sub>t m<sub>essages</sub> fr<sub>o</sub>m it<sub>s</sub> <sub>soc</sub>k<sub>e</sub>t int<sub>e</sub>rf<sub>ace</sub> <sub>a</sub>nd <sub>se</sub>nd<sub>s</sub> r<sub>espo</sub>n<sub>se</sub> messa<sub>g</sub>es into its socket interface<sub>.</sub> 

## A<sub>pp</sub>lication La<sub>y</sub>er HTTP<sub>:</sub> Trans<sub>p</sub>ort Protocol

• HTTP historicall<sub>y</sub> used TCP as a trans<sub>p</sub>ort <sub>p</sub>rotocol because there are several useful services are provided by TCP, most of all reliable data transfer. 

• R<sub>eca</sub>ll r<sub>e</sub>li<sub>a</sub>bilit<sub>y:</sub> TCP <sub>gua</sub>r<sub>an</sub>t<sub>ees</sub> HTTP r<sub>eques</sub>t/r<sub>esponse</sub> <sub>messages</sub> t<sub>o</sub> <sub>even</sub>t<sub>ua</sub>ll<sub>y</sub> <sub>a</sub>rri<sub>ve</sub> i<sub>n</sub>t<sub>ac</sub>t <sub>a</sub>t th<sub>e</sub> destination (if <sub>p</sub>ossible). 

• However, TCP services may slow down the communication, hence the recent implementation of HTTP uses also UDP as transport protocol: 

• It is estimated to be aro<sub>u</sub>nd 30% faster than TCP<sub>-</sub>onl<sub>y</sub> comm<sub>u</sub>nication<sub>.</sub> 

• It relies on QUIC (Quick UDP Internet Connection) protocol that implements reliability on top of UDP. 

• Here we see one of the great advantages of a layered architecture: HTTP-based <sub>app</sub>li<sub>ca</sub>ti<sub>o</sub>n<sub>s</sub> n<sub>ee</sub>d n<sub>o</sub>t <sub>wo</sub>rr<sub>y</sub> <sub>a</sub>b<sub>ou</sub>t r<sub>eac</sub>h<sub>a</sub>bilit<sub>y,</sub> d<sub>a</sub>t<sub>a</sub> l<sub>oss,</sub> <sub>e</sub>t<sub>c.</sub> 

• HTTP applications can be simpler (both logically and computationally), by delegating most of the work t<sub>o</sub> th<sub>e</sub> l<sub>owe</sub>r<sub>-</sub>l<sub>eve</sub>l <sub>s</sub>t<sub>ac</sub>k<sub>.</sub> 

## A<sub>pp</sub>lication La<sub>y</sub>er HTTP<sub>:</sub> Statelessness

• Simplicity is very important for HTTP-based servers dealing with large number of requests per second. 

• In average, a server runs around 1000 HTTP requests per second (large search engine infrastructures receive hundreds of thousands of queries per second!). 

• HTTP a<sub>pp</sub>lications are t<sub>yp</sub>icall<sub>y</sub> stateless<sub>:</sub> the server does not maintain an<sub>y</sub> information about the interaction (se<sub>q</sub>uence of re<sub>q</sub>uests/res<sub>p</sub>onses) with a <sub>spec</sub>ifi<sub>c</sub> <sub>c</sub>li<sub>e</sub>nt<sub>.</sub> 

• Example: if a client asks for the same object twice in a row, the server does not consider this request redundant, but it just resends the object, as it has completely for<sub>g</sub>oten the <sub>p</sub>ast<sub>.</sub> 

• Not all a<sub>pp</sub>lications are stateless<sub>,</sub> se<sub>v</sub>eral a<sub>pp</sub>lications are instead stateful<sub>.</sub> 

## A<sub>pp</sub>lication La<sub>y</sub>er HTTP<sub>:</sub> Persistent and Non<sub>-p</sub>ersistent Connections

• In man<sub>y</sub> a<sub>pp</sub>lications (such as HTTP-based)<sub>,</sub> the client and server ma<sub>y</sub> communicate for an extended period of time, by sending multiple pairs of request-response. 

• This flow of messa<sub>g</sub>es ma<sub>y</sub> be made back-to-back<sub>,</sub> <sub>p</sub>eriodicall<sub>y</sub> (at re<sub>g</sub>ular intervals)<sub>,</sub> or intermitentl<sub>y</sub>. 

• When rel<sub>y</sub>in<sub>g</sub> on a connection-oriented <sub>p</sub>rotocol (such as TCP or QUIC)<sub>,</sub> we can have: • Persistent connections<sub>:</sub> all re<sub>qu</sub>ests and their corres<sub>p</sub>ondin<sub>g</sub> res<sub>p</sub>onses are sent over the same connection<sub>.</sub> 

• Non-persistent connections: for each request-response pair a new connection is established. 

• By default, todays HTTP applications use persistent connections, while HTTP clients and <sub>se</sub>r<sub>ve</sub>r<sub>s</sub> <sub>c</sub>an b<sub>e</sub> <sub>co</sub>nfi<sub>gu</sub>r<sub>e</sub>d t<sub>o</sub> <sub>use</sub> n<sub>o</sub>n<sub>-pe</sub>r<sub>s</sub>i<sub>s</sub>t<sub>e</sub>nt <sub>co</sub>nn<sub>ec</sub>ti<sub>o</sub>n<sub>s</sub> if n<sub>ee</sub>d<sub>e</sub>d<sub>.</sub> Earl<sub>y</sub> <sub>ve</sub>r<sub>s</sub>i<sub>o</sub>n<sub>s</sub> <sub>o</sub>f HTTP (HTTP 1.0) used non-<sub>p</sub>ersistent connections b<sub>y</sub> default. 

## A<sub>pp</sub>lication La<sub>y</sub>er HTTP: Non-<sub>p</sub>ersistent Connection (Exam<sub>p</sub>le)

• In a non<sub>-p</sub>ersistent connection<sub>,</sub> the connection is closed every time a request is served (e.g., an object is sent). • We will see HTTP exam<sub>p</sub>les on TCP<sub>.</sub> 

• E<sub>x</sub>am<sub>p</sub>l<sub>e:</sub> a<sub>ssu</sub>m<sub>e</sub> t<sub>o</sub> a<sub>s</sub>k f<sub>o</sub>r a W<sub>e</sub>b <sub>p</sub>a<sub>ge</sub> <sub>co</sub>n<sub>s</sub>i<sub>s</sub>tin<sub>g</sub> <sub>o</sub>f a base HTML file and 10 JPEG ima<sub>g</sub>es (all 11 of these objects reside on the same server). 

• The URL for the base HTML file is<sub>:</sub> • ht<sub>p:</sub>//www<sub>.</sub>someschool<sub>.</sub>ed<sub>u</sub>/someDe<sub>p</sub>artment/home<sub>.</sub>inde<sub>x</sub> 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/d9e44a0ebdd4921f206c8cf945d4d94374664b0b604bb39d93c698a21abe7dd8.jpg)


## A<sub>pp</sub>lication La<sub>y</sub>er HTTP: Non-<sub>p</sub>ersistent Connection (Exam<sub>p</sub>le)

• The connection takes <sub>p</sub>lace as follows (with TCP): 

1. The HTTP client process initiates a TCP connection to the server www.someschool.edu on <sub>p</sub>ort number 80 (default HTTP <sub>p</sub>ort)<sub>,</sub> we will have two sockets: one at the client and one at the server<sub>.</sub> 

2. The HTTP client sends an HTTP request message to the server via its socket in<sub>c</sub>l<sub>u</sub>din<sub>g</sub> th<sub>e</sub> <sub>p</sub>ath nam<sub>e</sub> /<sub>so</sub>m<sub>e</sub>D<sub>ep</sub>artm<sub>e</sub>nt/h<sub>o</sub>m<sub>e.</sub>ind<sub>ex.</sub> 

3. The HTTP server process receives the request message via its socket, retrieves the object /someDe<sub>p</sub>artment/home.index (from RAM or disk)<sub>,</sub> encapsulates the object in an HTTP response message, and sends back the res<sub>p</sub>onse messa<sub>g</sub>e to the client via its socket<sub>.</sub> 

4. The HTTP server process tells TCP to close the TCP connection, the TCP will (later) terminate the connection once it is sure that the client has received the res<sub>p</sub>onse messa<sub>g</sub>e intact (reliabilit<sub>y</sub>). 

5. The HTTP client receives the response message. The TCP connection terminates. The message indicates that the encapsulated object is an HTML fil<sub>e.</sub> Th<sub>e</sub> <sub>c</sub>li<sub>e</sub>nt <sub>ex</sub>tr<sub>ac</sub>t<sub>s</sub> th<sub>e</sub> fil<sub>e</sub> fr<sub>o</sub>m th<sub>e</sub> r<sub>espo</sub>n<sub>se</sub> m<sub>essage,</sub> <sub>exa</sub>min<sub>es</sub> th<sub>e</sub> HTML file, and finds references to the 10 JPEG objects. 

6. The first four steps are then repeated for each of the referenced JPEG objects. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/7faad143547395d7c5e25285c0ed3f764df3f296bd606ca28914f893e50e6f16.jpg)


## A<sub>pp</sub>lication La<sub>y</sub>er HTTP: Non-<sub>p</sub>ersistent Connection (Exam<sub>p</sub>le)

• Since the connection does not persist over diferent objects, we need 11 TCP connection (and 11 <sub>p</sub>airs of sockets) to transfer the whole <sub>p</sub>a<sub>g</sub>e<sub>,</sub> hence the elements of a <sub>p</sub>a<sub>g</sub>e ma<sub>y</sub> arrive in diferent moments<sub>.</sub> 

• Note: HTTP defines only the communication protocol between the client HTTP <sub>p</sub>ro<sub>g</sub>ram and the server HTTP <sub>p</sub>ro<sub>g</sub>ram<sub>,</sub> not how contents are dis<sub>p</sub>la<sub>y</sub>ed<sub>.</sub> 

• The way web pages are displayed depends on the browser: two diferent browsers ma<sub>y</sub> inter<sub>p</sub>ret (hence<sub>,</sub> dis<sub>p</sub>la<sub>y</sub> to the user) a Web <sub>p</sub>a<sub>g</sub>e in somewhat diferent wa<sub>y</sub>s. 

• E<sub>.g.,</sub> <sub>w</sub>aitin<sub>g</sub> f<sub>o</sub>r th<sub>e</sub> <sub>w</sub>h<sub>o</sub>l<sub>e</sub> <sub>p</sub>a<sub>ge</sub> t<sub>o</sub> b<sub>e</sub> l<sub>o</sub>ad<sub>e</sub>d b<sub>e</sub>f<sub>o</sub>r<sub>e</sub> t<sub>o</sub> <sub>s</sub>h<sub>ow</sub> it<sub>,</sub> showin<sub>g</sub> it ste<sub>p</sub> b<sub>y</sub> ste<sub>p,</sub> etc<sub>.</sub> 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/de0ba5419a33e5bfc5234df52208b828471b4fbc57d2bd91fcdf101bfbb11840.jpg)


## A<sub>pp</sub>lication La<sub>y</sub>er HTTP: Non-<sub>p</sub>ersistent Connection (Exam<sub>p</sub>le)

• The diferent connections may be established in sequence or in parallel. 

• In this exam<sub>p</sub>le<sub>,</sub> once we know that 10 JPEG ima<sub>g</sub>es are needed (i.e.<sub>,</sub> the main <sub>p</sub>a<sub>g</sub>e is received)<sub>,</sub> we ma<sub>y</sub> download all of them in <sub>p</sub>arallel. 

• In modern browsers users may also configure the degree of <sub>pa</sub>r<sub>a</sub>ll<sub>e</sub>li<sub>s</sub>m in<sub>vo</sub>l<sub>ve</sub>d<sub>:</sub> 

• Most browsers o<sub>p</sub>en 5 to 10 <sub>p</sub>arallel TCP connections<sub>,</sub> and each of these connections handles one re<sub>qu</sub>est<sub>-</sub>res<sub>p</sub>onse transaction<sub>.</sub> 

• Clearly, the use of parallel connections shortens the response time but increases the computational cost. 

• Des<sub>p</sub>ite <sub>p</sub>arallelism<sub>,</sub> establishin<sub>g</sub> multi<sub>p</sub>le (TCP) connections ma<sub>y</sub> <sub>s</sub>till ind<sub>uce</sub> a <sub>s</sub>i<sub>g</sub>nifi<sub>c</sub>ant time overhead. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/6c7292388f993ff43b69d960fb9fb149674e8f22971558b5e133c55a5984d54d.jpg)


## A<sub>pp</sub>lication La<sub>y</sub>er HTTP: Non-<sub>p</sub>ersistent Connections (RTTs)

• It is dificult to precisely estimate times on Internet. We can estimate the o<sub>v</sub>erhead it takes to finali<sub>z</sub>e a HTML re<sub>q</sub>uest in terms of round-trip times (RTTs). 

• The RTT is the time it takes for a small <sub>p</sub>acket to tra<sub>v</sub>el fr<sub>o</sub>m <sub>c</sub>li<sub>e</sub>nt t<sub>o</sub> <sub>se</sub>r<sub>ve</sub>r <sub>a</sub>nd b<sub>ac</sub>k t<sub>o</sub> th<sub>e</sub> <sub>c</sub>li<sub>e</sub>nt<sub>.</sub> 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/dedda85e29f242753c83349b6ce0f952c37794cddfb56b8a9cc866a7996efb72.jpg)


• Wh<sub>e</sub>n <sub>a</sub> <sub>use</sub>r <sub>c</sub>li<sub>c</sub>k<sub>s</sub> <sub>o</sub>n <sub>a</sub> h<sub>ype</sub>rlink th<sub>e</sub> br<sub>owse</sub>r initi<sub>a</sub>t<sub>es</sub> <sub>a</sub> connection between with the Web server<sub>.</sub> 

• Assumin<sub>g</sub> a TCP-based re<sub>q</sub>uest (connection-oriented)<sub>,</sub> to ensure the connection a three-way handshake is performed… 

## A<sub>pp</sub>lication La<sub>y</sub>er HTTP: Non-<sub>p</sub>ersistent Connections (RTTs)

• TCP three-way handshake procedure is performed throu<sub>g</sub>h the followin<sub>g</sub> 3 ste<sub>p</sub>s<sub>:</sub> 

• The client sends a small TCP se<sub>g</sub>ment to the server<sub>,</sub> to si<sub>g</sub>nal that a connection is re<sub>qu</sub>ested<sub>.</sub> 

• Th<sub>e</sub> <sub>se</sub>r<sub>ve</sub>r a<sub>c</sub>kn<sub>ow</sub>l<sub>e</sub>d<sub>ges</sub> and r<sub>espo</sub>nd<sub>s</sub> <sub>w</sub>ith a <sub>s</sub>mall TCP se<sub>g</sub>ment<sub>.</sub> 

• Th<sub>e</sub> <sub>c</sub>li<sub>e</sub>nt a<sub>c</sub>kn<sub>ow</sub>l<sub>e</sub>d<sub>ges</sub> ba<sub>c</sub>k t<sub>o</sub> th<sub>e</sub> <sub>se</sub>r<sub>ve</sub>r<sub>.</sub> 

• From RTT’s <sub>p</sub>ers<sub>p</sub>ective<sub>,</sub> it takes 2 RTTs to establish a TCP connection (assumin<sub>g</sub> no <sub>p</sub>acket-loss). 

• N<sub>o</sub>ti<sub>ce</sub> that a <sub>s</sub>imilar hand<sub>s</sub>hak<sub>e</sub> al<sub>so</sub> tak<sub>es</sub> <sub>p</sub>la<sub>ce</sub> when connection is closed<sub>.</sub> 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/5acf8507c205b409adbcccca5ca1fc7057cefd93c45a2ac826af7bb9788a34be.jpg)


## A<sub>pp</sub>lication La<sub>y</sub>er HTTP: Non-<sub>p</sub>ersistent Connections (RTTs)

• The first two <sub>p</sub>arts of the three<sub>-</sub>wa<sub>y</sub> handshake take one RTT<sub>.</sub> 

• In HTTP<sub>,</sub> the client sends the HTTP request message combined with the third <sub>pa</sub>rt <sub>o</sub>f th<sub>e</sub> thr<sub>ee-way</sub> h<sub>a</sub>nd<sub>s</sub>h<sub>a</sub>k<sub>e</sub> (the acknowled<sub>g</sub>ment). 

• Once the re<sub>q</sub>uest messa<sub>g</sub>e arrives<sub>,</sub> the server sends the HTML file<sub>.</sub> This HTTP re<sub>qu</sub>est/res<sub>p</sub>onse eats <sub>up</sub> another RTT<sub>.</sub> 

• Rou<sub>g</sub>hl<sub>y,</sub> the total res<sub>p</sub>onse time is two RTTs plus the transmission time at the server of the HTML file<sub>.</sub> 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/f873e11ba9e3614d829bf66fadd249fe5bab3d119e56b0a5362fec21ff88fa7e.jpg)


## A<sub>pp</sub>lication La<sub>y</sub>er HTTP<sub>:</sub> Persistent Connections

• In persistent connections, the server leaves open the TCP connection after sendin<sub>g</sub> a res<sub>p</sub>onse<sub>.</sub> 

• Re<sub>q</sub>uests and res<sub>p</sub>onses between the same client and server can be sent over the same connection: an entire Web page (the HTML file and the 10 ima<sub>g</sub>es from the <sub>p</sub>revious example) can be sent over a single persistent TCP connection<sub>.</sub> 

• Multiple Web pages residing on the same server can also be <sub>se</sub>nt fr<sub>o</sub>m th<sub>e</sub> <sub>se</sub>r<sub>ve</sub>r t<sub>o</sub> th<sub>e</sub> <sub>sa</sub>m<sub>e</sub> <sub>c</sub>li<sub>e</sub>nt <sub>ove</sub>r <sub>a</sub> <sub>s</sub>in<sub>g</sub>l<sub>e</sub> <sub>p</sub>ersistent TCP connection<sub>.</sub> 

• Following this approach, we can save roughly 2-4 RRTs per object. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/9aec41c4b860bbbcfd23c254a6fa52b0249e1fe77037d66c9b871a794b3f1ddc.jpg)


## A<sub>pp</sub>lication La<sub>y</sub>er HTTP<sub>:</sub> Persistent Connections with Pi<sub>p</sub>elinin<sub>g</sub>

• Pipelining: requests for objects can be made backt<sub>o-</sub>ba<sub>c</sub>k<sub>,</sub> <sub>w</sub>ith<sub>ou</sub>t <sub>w</sub>aitin<sub>g</sub> f<sub>o</sub>r r<sub>ep</sub>li<sub>es</sub> t<sub>o</sub> <sub>pe</sub>ndin<sub>g</sub> requests. 

• In recent <sub>y</sub>ears (since HTTP/2) multi<sub>p</sub>le re<sub>q</sub>uests and r<sub>ep</sub>li<sub>es</sub> <sub>c</sub>an b<sub>e</sub> int<sub>e</sub>rl<sub>e</sub>a<sub>ve</sub>d in th<sub>e</sub> <sub>s</sub>am<sub>e</sub> <sub>co</sub>nn<sub>ec</sub>ti<sub>o</sub>n<sub>.</sub> 

• There is also a mechanism to <sub>p</sub>rioriti<sub>z</sub>e HTTP r<sub>eques</sub>t<sub>s</sub> <sub>a</sub>nd r<sub>ep</sub>li<sub>es</sub> <sub>w</sub>ithin thi<sub>s</sub> <sub>co</sub>nn<sub>ec</sub>ti<sub>o</sub>n<sub>.</sub> 

• Persistent connections with pipelining is currently the default mode in HTTP<sub>.</sub> 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/13494537d58f95d1c4a9901403e2dd190052332a3c6d7690ffa0450527382f31.jpg)


## A<sub>pp</sub>lication La<sub>y</sub>er HTTP<sub>:</sub> Persistent vs<sub>.</sub> Non<sub>-p</sub>ersistent Connections

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/8b4b14c4cddb229469c0a916d2881fd9f743084bccaf7e6a2ae812ee297be894.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/209e41adb6ab5232a20732ee0e8d8d986e9185056fac3f66baa28737d16b42fa.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ed62a200-81f6-4dd0-8f1f-f1063e9e557e/d666db1edc33052beaac1f7a042b7b7829d0f0f1e3ce1352e71625655afcce39.jpg)



Rou<sub>g</sub>h com<sub>p</sub>arison of RRTs n<sub>ee</sub>d<sub>e</sub>d t<sub>o</sub> r<sub>eques</sub>t 3 fil<sub>es</sub> <sub>co</sub>n<sub>s</sub>id<sub>e</sub>rin<sub>g</sub> th<sub>e</sub> 3 m<sub>o</sub>d<sub>a</sub>liti<sub>es</sub>


## A<sub>pp</sub>lication La<sub>y</sub>er HTTP<sub>:</sub> Persistent vs<sub>.</sub> Non<sub>-p</sub>ersistent Connections

## • Persistent<sub>:</sub>

• F<sub>as</sub>t<sub>e</sub>r<sub>,</sub> <sub>espec</sub>i<sub>a</sub>ll<sub>y</sub> <sub>us</sub>in<sub>g</sub> <sub>p</sub>i<sub>pe</sub>linin<sub>g.</sub> 

• Less resources needed (mostl<sub>y</sub> memor<sub>y</sub>). 

• M<sub>o</sub>r<sub>e</sub> <sub>co</sub>m<sub>p</sub>l<sub>ex</sub> t<sub>o</sub> im<sub>p</sub>l<sub>e</sub>m<sub>e</sub>nt<sub>,</sub> <sub>espec</sub>i<sub>a</sub>ll<sub>y</sub> <sub>us</sub>in<sub>g</sub> <sub>p</sub>i<sub>pe</sub>linin<sub>g.</sub> 

• Connection ma<sub>y</sub> be left o<sub>p</sub>en even if <sub>u</sub>n<sub>u</sub>sed<sub>.</sub> T<sub>yp</sub>icall<sub>y,</sub> the HTTP server closes a connection when it isn’t used for a certain time (timeout). 

## • Non<sub>-p</sub>ersistent<sub>:</sub>

• Eas<sub>y</sub> to im<sub>p</sub>lement and nicel<sub>y</sub> fitin<sub>g</sub> the statelessness of HTTP<sub>.</sub> 

• Needs more reso<sub>u</sub>rces<sub>,</sub> for each of these connections<sub>,</sub> TCP b<sub>u</sub>fers m<sub>u</sub>st be allocated <sub>a</sub>nd TCP <sub>va</sub>ri<sub>a</sub>bl<sub>es</sub> m<sub>us</sub>t b<sub>e</sub> k<sub>ep</sub>t in b<sub>o</sub>th th<sub>e</sub> <sub>c</sub>li<sub>e</sub>nt <sub>a</sub>nd <sub>se</sub>r<sub>ve</sub>r<sub>.</sub> 

• Slower<sub>,</sub> 1<sub>-</sub>2 additional RRTs needed <sub>p</sub>er re<sub>qu</sub>est<sub>.</sub> 

• Connections cannot be left o<sub>p</sub>en<sub>.</sub> 