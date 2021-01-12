import socket
import os 
import threading

#function to recive get request
def GET(name, sock):
     filename = sock.recv(1024)
	 if os.path.isfile(filename):
	        sock.send("EXIStS" + str(os.path.getsize(filename)))
			userResponse = sock.recv(1024)
			if userResponse [:2] == 'OK':
			       with open(filename,'rb') as f:
				           bytesToSend = f.read(1024)
						   sock.send(bytesToSend)
						   while bytesToSend != "":
						           bytesToSend = f.read(1024)
								   sock.send(bytesTosend)
				   #sock.send("HTTP/1.0 200 OK")		   
								  
	  else :
	         sock.send ("HTTP/1.0 404 Not Found\n")
			 
	  sock.close()
	  
	  return;
	  
	  
#function to recive post request
def POST(name,sock):
        filename = sock.recv(1024)
		if filename != 'q':
		        data = sock.resv(1024)
				if data [:6] == 'EXISTS':
				         filesize = long (data[6:])
						 print "file exits, uplouding...."
						 
						 sock.send('OK')
						 f = open('new_post_'+filename,'wb')
						 data = sock.recv(1024)
						 totalRecv = len(data)
						 f.write(data)
						 while totalRecv < filesize:
						        data = sock.recv(1024)
								totalREcv += len(data)
								f.write(data)
								print "{0:.2f}".format((totalRecv/float(filesize))*100)+"% Done"
								
						 print "uploud successful\n"
						 
					
				else :
				       print "error\n"
					   
		    sock.close()
			
			
			return;			   		 
							   
	 




# main function of the server
def Main():
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
port = 1234
address = (ip,port)
server.bind(address)
server.listen(5)
print "server started to listen on .....[",ip,"][",port,"]"
while True:
     client, addr = server.accept()
	 print "connection accepted from client"
	 clientrequest = server.recv(1024)
	 if clientrequest [:3] == 'GET':
	        t = threading.Thread(target=GET,args=("GETthread", client))
			t.start()
	 elif clientrequest [:3] == 'POST':
	       #post thread
		   t2 = threading.Thread(target=POST,args("POSTthread",client))
		   t2.start()
	 else :
	       print "error:request is wrong, not found"
server.close()
  	 
if __name__== '__main__' :
      Main()
