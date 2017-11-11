# A-pythonic-web-server
A multi-threaded HTTP server written in python that accepts HTTP GET requests and returns the desired content to the client

Functions.
1. Creates a TCP server socket to listen for incoming TCP connections from clients and
establishes a TCP connection.
2. For better throughput different requests are handled by different threads, with a new
thread created for each client request.
3. Server's access log shows client IP, client port and number of times a particular file
was accessed.

References
1. Socket programming - https://docs.python.org/2/howto/sockets.html
2. Accepting,binding and closing socket connections - https://docs.python.org/3/library/socket.html#socket.socket.accept
3. Multithreading - https://www.tutorialspoint.com/python/python_multithreading.htm
4. Last modification time - https://docs.python.org/3/library/os.path.html#os.path.getmtime
5. HTTP headers - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
