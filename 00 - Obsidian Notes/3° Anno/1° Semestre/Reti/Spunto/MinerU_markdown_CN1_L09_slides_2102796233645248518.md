## The Application Layer: Network programming and DNS

Lecture 9 

## Application Layer Creating Network Applications

• Sockets are a central element for the creation of network applications. 

• They typically manages (black-box) the transport (UDP/TCP) and the network (IP) layers functionalities. 

• Note that there are several applications (middleware) that may wrap sockets simplifying their creation and providing more complex functionalities. 

• However, basic API are still widely used. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0ffcfcfe-3741-4f08-96fe-f52821c1b770/bd36e9cbd49903b6858b8b46a49eff061c79049b74bff3a5b8cefdf9d565ae87.jpg)



Where layers are implemented


## Application Layer Connection-oriented vs. Connectionless

Client 

Server 

Create Socket 

Create Socket 

Send Message 

Read Message 

Send Reply 

Connectionless (UDP) 

Close Socket 

Connection Oriented (TCP) 

Creation 

Connection 

Read Reply 

Messaging 

Destruction 

Client 

Connect 

Create Socket 

Send Message 

Read Message 

Read Reply 

Server 

Wait Connections 

Close Socket 

Create Socket 

Send Reply 

Close Client-specific Socket 

## Application Layer UDP Socket Commands

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0ffcfcfe-3741-4f08-96fe-f52821c1b770/6323aa7c0803bb6ae255e7ff4c3cebc0e7499d2553d014a02c0e12bbfdd7aee4.jpg)


• For UDP connection we need both client and server to open a socket. 

• The server has to bind the socket to a specific port. 

• Then we can exchange messages using sendto and recvfrom functions. 

• Here IP and port of the client are retrieved through the recvfrom function. 

• We may loop over sendto/recvfrom to keep alive the communication. 

• When communication is over, both hosts close the socket. 

• Notice that if client only closes the socket, the server may accept other clients. 

## Application Layer TCP Socket Commands

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0ffcfcfe-3741-4f08-96fe-f52821c1b770/33a81e57b0d4dad4e44c19867e458723c47c2a92d70d61d34ced1496602c69f2.jpg)


• For TCP connection we need both client and server to open a socket. 

• The server has to bind the socket to a specific port, listen and eventually accept new connection. The client has to connect to the server. 

• Then we can exchange messages using send and read functions. 

• Here IP and port of the client are retrieved from the newly created socket. 

• We may loop over send/read to keep alive the communication. 

• When communication is over, both hosts close the socket. 

• Notice that the server should perform an additional read before to close the client-specific socket (connection release) otherwise we must wait about 4 minutes to reuse the port. 

• The server may also go back to the accept function and welcome another client. 

## Application Layer DNS Translation (C/C++)

• As just shown, we can create sockets between two hosts, but we need to know (IP) address and port of the server. 

• On the Internet, hosts are typically identified by hostnames rather than by IP addresses. 

• Berkeley sockets (C/C++) only works with IP addresses. 

• This is not surprising as sockets works on transport layer, while hostnames works on application layer. 

• If we are to connect with a host by hostname, we need to use DNS translation and get the associated IP address to be passed to the socket. 

## Application Layer DNS Translation (C/C++)

• C/C++ ofers some functions and structures that perform such translation for us, which are used to contact DNS servers and to retrieve addresses. 

• In particular, we can use the function gethostbyname() to contact DNS servers. 

• The above function does not return just the IP address. It returns a hostent structure that contains some info about the host: 

• Canonical name. 

• Possible aliases. 

• One or more addresses. 

## Application Layer DNS Translation (C/C++)

## • The hostent structure is defined as follows:

```c
#include <netdb.h>

struct hostent {
    char * h_name; // original name of the host (canonical)
    char ** h_aliases; // list of aliases (terminated by a NULL pointer)
    int h_addrtype; // family of the address (typically AF_INET)
    int h_length; // length of the address (typically 4 bytes)
    char ** h_addr_list; // list of addresses (terminated by a NULL pointer)
};

// for compatibility reasons
#define h_addr h_addr_list[0] 
```

• A DNS may provide a list of addresses (which may be randomly ordered if the query is sent to round-robin DNS servers). 

• We can get the address of the first element of the array (h_addr_list[0] or h_addr). 

• The returned addresses can be casted to in_addr structure used by sockets. 

## Application Layer DNS Translation (C/C++)

## • The gethostbyname() function is defined as follows:

```c
#include <netdb.h>

struct hostent *host_info = gethostbyname(const char *name); 
```

## • Where:

• name: is a string containing the hostname to be translated. 

• host_info: is a pointer to the hostent structure containing the information about host. • This is NULL if error occurred. 

• Notice that there is also a similar function gethostbyaddr() that returns a hostent structure for a specified IP address. 

## Application Layer DNS Translation (C/C++)

```c
#include <iostream>
#include <cstring>
#include <string>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <unistd.h>
#include <netdb.h>
#include <stdio.h> 
```

```cpp
int main(int argc, char **argv){
    struct hostent *server_info;
    char *server_name;

    if (argc < 2){
    std::cout << "No hostname specified" << std::endl;
    return 0;
    }
    else {
    server_name = argv[1];
    }

    server_info = gethostbyname(server_name);
    if (server_name == NULL){
    std::cout << "could Not resolve hostname " << server_name << " :(" << std::endl;
    return 0;
    } 
```

## • Include libraries to allow DNS translation.

• Initialization. 

• Get hostname as argument. 

• Invoke DNS and check if a response has been received. 

## Application Layer DNS Translation (C/C++)

```objectivec
//plot output
std::cout<<"Canonical name:"<<std::endl;
std::cout<<"\t"<<server_info->h_name<<std::endl;

std::cout<<"Aliases:"<<std::endl;
int i = 0;
while(server_info->h_aliases[i] != NULL){
    std::cout<<"\t"<<server_info->h_aliases[i]<<std::endl;
    i++;
}

std::cout<<"IPs:"<<std::endl;
i = 0;
while(server_info->h_addr_list[i] != NULL){
    std::cout<<"\t"<<inet_ntoa( *( (struct in_addr *) server_info->h_addr_list[i] ) ) "<<std::endl;
    i++;
}

return 0;
} 
```

## • Ploting output from hostent structure:

• Canonical name. 

• List of aliases 

• List of IPs. 

• We will now create a C++ code implementing from scratch a HTTP request (HEAD) for a web page. 

• The web page we will check is the “cenni storici” from the UNINA website: 

• htp://www.unina.it/chi-siamo/cenni-storici 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0ffcfcfe-3741-4f08-96fe-f52821c1b770/e6ad1284954a2c17a4d638e699bfb8921efd439fa9fde8e924cc2fb07fbbfdaa.jpg)


STUDENTIDOCENTIPERSONALE 

Home 

Chi slamoAteneoDidatticaRicercaTerza Misslione F2Magazine InternationalStudiaUNINA 

Cenni storici 

HOME > CHI SIAMO > CENNI STORICI 

CENNI STORICI 

PATRIMONIO ARCHITETTONICO 

## L'Università degli Studi di Napoli Federico II

È dal 1992 che l'Università di Napoli è stata Intitolata a Federico II, a sottolineare le sue antichissime origini, risalenti al 5 glugno 1224, quando l'Imperatore svevo, nonche re di Sicilla, da Siracusa emano l'editto Istitutivo. A differenza che a Bologna e In altre città, lo Studlo napoletano nacque con un atto Imperlale, volto a formare I gruppi dirigenti necessarl al governo dello Stato. Questa origine laica non avrebbe pero Impedito pesanti Intromissloni della Chiesa nella sua vita culturale. 

La storla plurisecolare dell'Università di Napoll ebbe molti momenti oscurl e battute d'arresto, ma anche slanci Innovativi che attirarono sul suol doçenti l'attenzione del mondo universitarlo e accademico europeo. Anche nelle fasi plù difficili mal perse la forza di attrazione su una popolazione studentesca provinciale che nella formazione universitaria vedeva delle prospettive di ascesa sociale e di elevazione culturale. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0ffcfcfe-3741-4f08-96fe-f52821c1b770/ae5e210b47934254d55656d509581173160c52a452c603622db854b520ee6ed6.jpg)


SCARICA L'ARTICOLO COMPLETO 

## Amministrazlone Trasparente

Disposizioni generali 

Organizzazione 

Performance 

Consulenti e cllaboratori 

Enti controllati 

Personale 

Bandi di concorso 

Bilanci 

Attivita e procedimenti 

Bandi di gara e contratti 

Sowvenzioni, contributi, sussidi,Prowvedimenti vantaggi economici 

Controlli e rilievi sull'Amministrazione Beni immobili e gestione patrimonio 

Servizi erogati 

Pagamenti dell'ammninistrazione 

Altri contenuti 

Opere pubbliche 

Atti di notifica 

P.IA.O. di Ateneo 

## Contattl

PEC ateneo@pec.unina.it 

Segreterie studenti (riscontri titoli studiol 

Indirizzi email e PEC istituzionali 

Servizio UNINAPEC 

URP 

Organigramma 

Rubrica 

Sedi 

Centro Congressi 

Albo ufficiale 

Accesso civico - FOIA 

Area riservata 

Guida al portale 

Mappa del portale 

Accessibilita 

Elenco Siti tematici 

Informativa sui cookie 

Modulistica 

Privacy - Data breach 

## Application Layer HTTP Socket Example (C/C++)

```c
#include <iostream>
#include <cstring>
#include <string>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <unistd.h>
#include <netdb.h>
#include <stdio.h> 
```

```cpp
int main(){
    int socket_desc;
    struct sockaddr_in serv_addr;
    struct hostent *server;
    char buffer[4096];

    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_desc < 0){
    std::cout << "failed to create socket" << std::endl;
    return 0;
    } 
```

• Include libraries to allow TCP connection to the web server. 

• Initialize variables and create the TCP socket. For a HTTP request 3 elements are specified: 

• Hostname of the web server. 

• Port number. 

• Resource to be retrieved (object’s path). 

• Note: here we use the C++ cout for simplicity. 

## Application Layer HTTP Socket Example (C/C++)

```cpp
server = gethostbyname("www.unina.it");
if (server == NULL){
    std::cout << "could Not resolve hostname :;"
    << std::endl;
    close(socket_desc);
    return 0;
}

bzero((char *) &serv_addr, sizeof(serv_addr));
serv_addr.sin_family = AF_INET;
serv_addr.sin_port = htons(80);
bcopy((char *) server->h_addr, (char *)&serv_addr.sin_addr.s_addr, server->h_length);

if (connect(socket_desc, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0){
    std::cout << "connection failed :(" << std::endl;
    close(socket_desc);
    return 0;
} 
```

• Connection to the web server. Here we use the following function: 

```txt
server =
gethostbyname(host.c_str()); 
```

that invokes DNS and to gets the IP of the server from the hostname (inside the hostent struct). 

• The IP from the returned structure is copied into the serv_addr structure for the following connect function. 

## Application Layer HTTP Socket Example (C/C++)

```cpp
const char *request = "HEAD /chi-siamo/cenni-storici HTTP/1.1\r\nHost: www.unina.it\r\nConnection: close\r\n\r\n";

if (send(socket_desc, request, strlen(request), 0) < 0){
    std::cout << "failed to send request..." << std::endl;
    close(socket_desc);
    return 0;
}
std::cout<<"message sent:"<<std::endl;
std::cout<<request<<std::endl;

int n = recv(socket_desc, buffer, sizeof(buffer), 0); 
```

```cpp
std::cout<<"received "<<n<<" bytes:"<<std::endl;
std::cout<<buffer;

close(socket_desc);

return 0; 
```

## <sup>•</sup> Messaging with the web server. The HTTP request is defined into the request string.

<sup>•</sup> Here we are creating a non-persistent connection since we just want to check one page. 

• Close socket and plot the received page (HTML). 