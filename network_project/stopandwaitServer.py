import time,socket,random,os,checksum
from threading import Thread

def clientDef(addr):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.connect(addr)

    f = open(filename, 'r')
    fileSize = os.stat(filename).st_size
    server_socket.sendto(str(fileSize).encode(), addr)  # send size of file to client by string
    starting_time = time.time()
    seq = -1
    receivedseq = -1
    trans = 0
    buffer = None
    server_socket.settimeout(2)
    while trans < fileSize:

        if receivedseq == seq:
            seq += 1
            buffer = f.read(20)

        if random.random() >= lossp:  # normal send
            packet = str(seq) + "`" + buffer + "`" + str(
                checksum.calc_checksum(str(seq) + buffer) + random.randint(0, 1))
            server_socket.sendto(packet.encode(), addr)

        try:
            receivedpacket, addr = server_socket.recvfrom(100)  # wait for ack
            receivedseq = int(receivedpacket.decode())  # if ack arrivs do
            if receivedseq == seq:
                trans += 20
                if trans > fileSize:
                    trans = fileSize
                print("sent packet: " + str(seq))
        except socket.timeout as e:  # if no ack and time out
            print(e)

    end_time = time.time()
    print("Finished")
    print("Time elapsed: ", str(end_time - starting_time))


port = 3000
seed = 90
random.seed(seed)
windowsize = 10
lossp = 0.1
IP = socket.gethostbyname('localhost')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((IP, port))

while 1:
    filename, addr = server_socket.recvfrom(100)
    t1 = Thread(target=clientDef,args=(addr,))
    t1.start()
