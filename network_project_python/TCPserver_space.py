import socket
import os 
import threading

threads = []
#function to recive get request
def GET(name, sock):
		 filename = sock.recv(1024)
		 filename.decode("utf-8")
		 if os.path.isfile(filename):
						request = "EXIStS" + str(os.path.getsize(filename))
						sock.send(bytes(request,"utf-8"))
						userResponse = sock.recv(1024)
						if userResponse [:2] == 'OK':
									 with open(filename,'rb') as f:
													 bytesToSend = f.read(1024)
													 sock.send(bytesToSend)
													 while bytesToSend != "":
																	 bytesToSend = f.read(1024)
																	 sock.send(bytesToSend)
									 #sock.send("HTTP/1.0 200 OK")           
																	
		 else:
				sock.send ("HTTP/1.0 404 Not Found\n")
						 
		 sock.close()
			
		 return;
			
			
#function to recive post request
def POST(name,sock):
				filename = sock.recv(1024)
				filename.decode("utf-8")
				if filename != 'q':
								data = sock.recv(1024)
								if data [:6] == 'EXISTS':
												 filesize = long(data[6:])
												 print ("file exits, uplouding....")
												 
												 sock.send('OK')
												 f = open('new_post_'+filename,'wb')
												 data = sock.recv(1024)
												 totalRecv = len(data)
												 f.write(data)
												 while totalRecv < filesize:
																data = sock.recv(1024)
																totalRecv += len(data)
																f.write(data)
																print ("{0:.2f}".format((totalRecv/float(filesize))*100)+"% Done")
																
												 print ("uploud successful\n")
												 
										
								else :
											 print ("error\n")
											 
				sock.close()
						
						
				return;                  
															 
		 




# main function of the server
def Main():
				server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				ip=socket.gethostbyname(socket.gethostname())
				port=1234
				address=(ip,port)
				server.bind(address)
				server.listen(5)
				print ("server started to listen on .....[",ip,"][",port,"]")
				#client, addr = server.accept()
				while True:
								client, addr = server.accept()
								print ("connection accepted from client")
								clientrequest = client.recv(1024)
								print(clientrequest)
								clientrequest.decode("utf-8")
								print(clientrequest)
								if clientrequest ==b'GET':
									print("thread will start")
									t = threading.Thread(target=GET,args=("GET", client))
									t.start()
									threads.append(t)
								elif clientrequest ==b'POST':
								  t2 = threading.Thread(target=POST,args=("POST",client))
								  t2.start()
								  threads.append(t2)
								else:
									print("error:request is wrong, not found")
				for t in threads:
					t.join()
				server.close()

if __name__== '__main__' :
	Main()


input()


								 
