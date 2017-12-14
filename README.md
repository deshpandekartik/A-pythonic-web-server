# A-pythonic-web-server
A multi-threaded HTTP server written in python that accepts HTTP GET requests and returns the desired content to the client

## Summary

Functions.
- Creates a TCP server socket to listen for incoming TCP connections from clients and
establishes a TCP connection.
- For better throughput different requests are handled by different threads, with a new
thread created for each client request.
- Server's access log shows client IP, client port and number of times a particular file
was accessed.

## Getting Started

To start pythonic-web-server-:

- Create www directory ( mkdir www ) and place sample html files into it. 
- python server.py 80

Sample input / Output

Input

```
kdeshpa3@remote06:~/distributedNetworks/kdeshpa3-p1$ wget remote06.cs.binghamton.edu:10000/index.html
--2017-09-19 20:25:47--  http://remote06.cs.binghamton.edu:10000/index.html
Resolving remote06.cs.binghamton.edu (remote06.cs.binghamton.edu)... 128.226.180.168
Connecting to remote06.cs.binghamton.edu (remote06.cs.binghamton.edu)|128.226.180.168|:10000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 97 [text/html]
Saving to: 'index.html1'
index.html1                              100%[=====================================================================================>]      97  --.-KB/s    in 0s
2017-09-19 20:25:47 (10.4 MB/s) - 'index.html.1' saved [97/97]


➜  localhost:10000/sample.html
<html>
<head>
<title>File Not Found</title>
</head>
<body>
<center><b>The requested file could not be found</b></center>
</body>
</html>



```

Output Server access log ( Format : filename | client IP  | client port | access count )

```
index.html|127.0.0.1|59630|1
test.html|127.0.0.1|59632|1
test.html|127.0.0.1|59634|2
sample.html|127.0.0.1|59636|1
test/folder.html|127.0.0.1|59644|1
test/activa.jpg|127.0.0.1|59646|1
```
## References
1. Socket programming - https://docs.python.org/2/howto/sockets.html
2. Accepting,binding and closing socket connections - https://docs.python.org/3/library/socket.html#socket.socket.accept
3. Multithreading - https://www.tutorialspoint.com/python/python_multithreading.htm
4. Last modification time - https://docs.python.org/3/library/os.path.html#os.path.getmtime
5. HTTP headers - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers

### Contact

[Kartik Deshpande](https://www.linkedin.com/in/kartik-deshpande/)

