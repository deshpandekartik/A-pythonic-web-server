#!/usr/bin/python

import socket 
import os
import thread # for multithreading
import sys
import mimetypes # to find mime type of a file
import datetime
from mimetools import Message
CounterList = []

######################################## Defining Variables
MAX_RECEVIE_BYTES = 1024

######################################## increment counter on per access file
def Accesscounter(CounterList, reqfile,clientaddress):
	CounterList.append(reqfile)
	accesscount = CounterList.count(reqfile)
	accesslog = reqfile + "|" + '|'.join(str(x) for x in clientaddress) + '|' + str(accesscount)
	print accesslog

######################################### Function to respond to client's incomming request
def respond_client(clientsocket,clientaddress):
	request = clientsocket.recv(MAX_RECEVIE_BYTES) # read the client request

	if request != "":
		reqfile = request.split()[1] #get the html file request via GET parameters
		reqfile = reqfile[1:].strip()
	else:
		reqfile = ""

	if reqfile == "":
		reqfile = "index.html"

	if os.path.isfile(os.getcwd() + "/" + reqfile) :

                thread.start_new_thread(Accesscounter, (CounterList,reqfile,clientaddress))

                # if the www directory has the requested file
		filedescriptor = open(reqfile)
		filecontent = filedescriptor.read()
		filedescriptor.close()

		# prepare all data to be sent in http response header
		mimetype,fileEncoding = mimetypes.guess_type(reqfile) # get mime type of requested file
		todaysdate = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT') # get current date and time
		modificationtime = datetime.datetime.utcfromtimestamp(os.path.getmtime(reqfile)).strftime('%a, %d %b %Y %H:%M:%S GMT')
                responsecontent = "HTTP/1.0 200 OK \nDate:" + todaysdate + " \nServer:Python0.0 \nLast-Modified:" + modificationtime + " \nContent-Type:" + mimetype + " \nContent-Length:" + str(os.path.getsize(reqfile)) + "\r\n\n"
		for i in range(0, len(filecontent)):
			responsecontent = responsecontent + filecontent[i]
		clientsocket.send(responsecontent)
		clientsocket.close()
	
	else:
		reqfile = ""
		clientsocket.send("""HTTP/1.0 404 ERR
Content-Type: text/html

<html>
<head>
<title>File Not Found</title>
</head>
<body>
<center><b>The requested file could not be found</b></center>
</body>
</html>
""")
		clientsocket.close()



####################################### To check if www directory exist in current directory
if not os.path.isdir(os.getcwd() + "/www/"):
	print "ABORT ! Directory www does not exist in PWD. To create a directory mkdir www/"
	sys.exit(0)
else:
	web_dir = os.getcwd() + "/www/"
	os.chdir(web_dir)


if len(sys.argv) != 2:
	print "Please specify a port number"
	sys.exit(0)

try:
	BIND_PORT = int(sys.argv[1]) #port to which  this python web server will bind to
except:
	print "Port number should be a valid integer"

######################################## Bind this server to specified port 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
        serversocket.bind(('',BIND_PORT))
except socket.error, msg:
        print "ABORT ! Port " + str(BIND_PORT) + " is already in use ! To change the port edit server.py file and change BIND_PORT variable value" 
        sys.exit(0)
serversocket.listen(1)          # max one queed requests when server is busy
print socket.gethostname() + " serving at port " + str(BIND_PORT)

######################################## Accept incoming client connections and call function to handle them ( via multithreading )
while 1:
	clientsocket, clientaddress = serversocket.accept()   #clientsocket is a new socket object, var clientaddress is client's clientaddress
	thread.start_new_thread(respond_client, (clientsocket, clientaddress))



###################################
# References
# 1. Socket programming - https://docs.python.org/2/howto/sockets.html
# 2. Accepting,binding and closing socket connections - https://docs.python.org/3/library/socket.html#socket.socket.accept
# 3. Multithreading , Running several instances of function parallely - https://www.tutorialspoint.com/python/python_multithreading.htm
# 4. Last modification time - https://docs.python.org/3/library/os.path.html#os.path.getmtime
