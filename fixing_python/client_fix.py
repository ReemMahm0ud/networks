import socket
#import threading
import os



def Main():
        #userinput = input("choose : [1]GET   [2]POST : -> ")
        #try:
           # val = int(userinput)
           # print ("okay...sending....\n")
        #except ValueError:
            #print ("that's not a number(integer) ..try again next time\n")   
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ip=socket.gethostbyname(socket.gethostname())
        port=1234
        address=(ip,port)
        client.connect(address)
        filename = input("enter filename with the type please : ")
        if filename != 'q':
                client.send(bytes(filename,"utf-8"))
                data = client.recv(1024)
                data.decode("utf-8")
                if data[:6] == 'EXISTS':
                    filesize = long(data[6:])
                    print ("GET " +filename+" ",gethostname(), "... downloading file...\n ")
                    client.send("OK")
                    f = open('new_get_'+filename, 'wb')
                    data = client.recv(1024)
                    totalRecv = len(data)
                    f.write(data)
                    while totalRecv < filesize :
                        data = client.recv(1024)
                        totalRecv += len(data)
                        f.write(data)
                        print ("{0:.2f}".format((totalRecv/float(filesize))*100)+"% done..")
                        print ("HTTP/1.0 200 OK\n")
                else:
                    print ("file not found 404\n")
        client.close()          

if __name__== '__main__':
            Main()                      