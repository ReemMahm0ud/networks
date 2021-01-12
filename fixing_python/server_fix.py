import socket
import os 
import threading

#function to recive get request
def GET(name, sock):
         filename = sock.recv(1024)
         filename.decode("utf-8")
         if os.path.isfile(filename):
                        sock.send(bytes("EXIStS" + str(os.path.getsize(filename)),"utf-8"))
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
                                #clientrequest = client.recv(1024)
                                #clientrequest.decode("utf-8")
                                #if clientrequest =="GET":
                                t = threading.Thread(target=GET,args=("GETthread", client))
                                t.start()
                                #else: #clientrequest [:3]=='POST'
                                  #t2 = threading.Thread(target=POST,args=("POSTthread",client))
                                  #t2.start()
                                #else:
                                    #print("error:request is wrong, not found")
                server.close()

if __name__== '__main__' :
    Main()

