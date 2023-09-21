# FLASK

## What Is Flask?
Flask is a lightweight WSGI web application framework. It is designed to make getting started 
quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper 
around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

### WSGI
The Web Server Gateway Interface (Web Server Gateway Interface, WSGI) has been used as a standard 
for Python web application development. WSGI is the specification of a common interface between 
web servers and web applications.

### Werkzeug
Werkzeug is a WSGI toolkit that implements requests, response objects, and utility functions. This 
enables a web frame to be built on it. The Flask framework uses Werkzeg as one of its bases.

### jinja2
jinja2 is a popular template engine for Python.A web template system combines a template with a 
specific data source to render a dynamic web page.

## REST APIs
An API, or application programming interface, is a set of rules that define how applications or 
devices can connect to and communicate with each other. A REST API is an API that conforms to the 
design principles of the REST, or representational state transfer architectural style. For this 
reason, REST APIs are sometimes referred to RESTful APIs.

At the most basic level, an API is a mechanism that enables an application or service to access 
a resource within another application or service. The application or service doing the accessing 
is called the client, and the application or service containing the resource is called the server.

Some APIs, such as SOAP or XML-RPC, impose a strict framework on developers. But REST APIs can be 
developed using virtually any programming language and support a variety of data formats. The only 
requirement is that they align to the following six REST design principles - also known as 
architectural constraints:
1.  <b>Uniform interface</b>: All API requests for the same resource should look the same, no 
    matter where the request comes from. The REST API should ensure that the same piece of data, 
    such as the name or email address of a user, belongs to only one uniform resource identifier 
    (URI). Resources shouldn’t be too large but should contain every piece of information that the 
    client might need.
    
2. <b>Client-server decoupling</b>: In REST API design, client and server applications must be 
   completely independent of each other. The only information the client application should know 
   is the URI of the requested resource; it can't interact with the server application in any 
   other ways. Similarly, a server application shouldn't modify the client application other 
   than passing it to the requested data via HTTP.
    
3. <b>Statelessness</b>: REST APIs are stateless, meaning that each request needs to include all 
   the 
   information necessary for processing it. In other words, REST APIs do not require any 
   server-side sessions. Server applications aren’t allowed to store any data related to a 
   client request.
    
4. <b>Cacheability</b>: When possible, resources should be cacheable on the client or server side. 
   Server responses also need to contain information about whether caching is allowed for the 
   delivered resource. The goal is to improve performance on the client side, while increasing 
   scalability on the server side.
    
5. <b>Layered system architecture</b>: In REST APIs, the calls and responses go through different 
   layers. As a rule of thumb, don’t assume that the client and server applications connect 
   directly to each other. There may be a number of different intermediaries in the 
   communication loop. REST APIs need to be designed so that neither the client nor the server 
   can tell whether it communicates with the end application or an intermediary.
    
6. <b>Code on demand</b> (optional). REST APIs usually send static resources, but in certain 
   cases, responses can also contain executable code (such as Java applets). In these cases, 
   the code should only run on-demand.

### REST API Methods
These HTTP methods are used with REST APIs:

| Method 	   |                   Description                    |
|:-----------:|:------------------------------------------------:|
|   GET 	   | Retrieve information about the REST API resource |
|  POST 	   |            Create a REST API resource            |
|   PUT 	   |            Update a REST API resource            |
| DELETE 	   | Delete a REST API resource or related component  |

## Advantages of using Flask framework are:

- There is a built-in development server and a fast debugger provided.
- Lightweight
- Secure cookies are supported.
- Templating using Jinja2.
- Request dispatching using REST.
- Support for unit testing is built-in.


## Bring up Flask
###### Note: Please make the following changes in the Dockerfile 
```
ENV POSTGRES_HOST='127.0.0.1'
In the above line replace '127.0.0.1' with your local system ip
```
Build docker image
```
docker build -t ws3 .
```
Bring up flask app
```
docker run -p 5000:5000 "ws3:latest"
```


