import time,socket,checksum


IP = "localhost"
serverport = 3000
port = 4444
filename = "file.txt"
windowsize = 10

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (IP, serverport)
client_socket.bind((IP,port))
client_socket.settimeout(2)

client_socket.sendto(filename.encode(),server_addr)
received = 0
seq = 0 # first seq num recvd correct
receivedseq = -1
filesize,addr = client_socket.recvfrom(100)
filesize = int(filesize)
starting_time = time.time()
f = open("output.txt", 'w')

while received < filesize:
    try:
        buffer,addr = client_socket.recvfrom(100)
        buffer = buffer.decode().split("`")
        receivedseq = int(buffer[0])
        data = buffer[1]
        check__sum = float(buffer[2])
        if not checksum.checksum(check__sum,receivedseq,data): #check for errors
            print("something's wrong with the packet")
            client_socket.sendto(str(receivedseq-1).encode(),addr) #
            continue
        client_socket.sendto(str(receivedseq).encode(),addr) #wrong seq is send
        f.write(data)
        received += 20
        if received > filesize:
            received = filesize
        print("received packet: " + str(receivedseq))
        seq += 1
    except socket.timeout as e:
        print(e)
end_time = time.time()
print("Finished")
print("Time elapsed: ", str(end_time - starting_time))
f.close()
