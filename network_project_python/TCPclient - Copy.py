import socket
import threading
import os

#def POST(name,sock):
 #       filename =





def Main():
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		ip = socket.gethostbyname(socket.gethostname())
		port = 1234
		address = (ip,port)
		client.connect(address)
		
		userinput = input("choose : [1]POST   [2]POST : -> ")
		try:
		    val = int(userinput)
			print ("okay...sending....\n")
		except ValueError:
		       print ("that's not a number(integer) ..try again next time\n")
			   
		if userinput ==	'1'
		         client.send("GET")
	             filename = raw_input("enter filename with the type please : ")
		         if filename != 'q':
		         client.send(filename)
				 data = client.recv(1024)
				 if data[:6] == 'EXISTS':
				       filesize = long(data[6:])
				       print ("GET " +filename+" "+gethostname()+ "... downloading file...\n ")
			           client.send("OK")
				       f = open('new_get_'+filename, 'wb')
				       data = client.recv(1024)
				       totalRecv = len(data)
				       f.write(data)
				       while totalRecv < fileesize :
				               data = client.recv(1024)
					           totalRecv += len(data)
					           f.write(data)
			     	           print "{0:.2f}".format((totalRecv/float(filesize))*100)+"% done.."
					   
			           print ("HTTP/1.0 200 OK\n")
					   
				 else :
				       print ("file not found 404\n")
					   
				 client.close()
				
					   
		elif userinput == '2'
		          	#post function
					client.send("POST")
					filename = raw_input("enter filename with the type please : ")
					if os.path.isfile(filename):
					          client.send(filename)
					          print ("POST" +filename+" "+gethostname()+ "... uplouding file...\n ")
					          client.send("EXIStS" + str(os.path.getsize(filename)))
							  usrResponse = client.recv(1024)
							  if userResponse[:2] == 'OK' :
							         with open(filename, 'rb') as f:
									          bytesToSend = f.read(1024)
											  client.send(bytesToSend)
											  while bytesToSend != "": 
											          bytesToSend = f.read(1024)
													  client.send(bytesToSend)
													  
							
					else:
					     print "file don't exist"
						 
						 
					client.close()
						 						  
		
		else :
		      print("error...only choose between 1 or 2...try again")			
					


if __name__== '__main__':
        	Main()