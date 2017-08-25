# server file

import socket
from threading import Thread
# from socketserver import ThreadingMixIn

# declaring global vars for socket objects
TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024


class ClientThread(Thread):
    # overriding constructor for Thread
    def __init__(self, ip, port, sock):
        # invoke base class constructor before anything
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print('new thread started for ' + ip + ': ' + str(port) + ' ' +
              str(sock))

    def run(self):
        filename = 'mytext.txt'
        f = open(filename, 'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                print('sent ', repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break


# create socket object
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# adding options for sock obj so it won't wait for timeout
# before creating another socket connection
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind socket obj to local port
tcpsock.bind((TCP_IP, TCP_PORT))
# creating list of threads for further use
threads = []

# loop for creating passive connections with clients
while True:
    tcpsock.listen(5)
    print('waiting for incoming connections...')
    (conn, (ip, port)) = tcpsock.accept()
    print('got connection from ', (ip, port))
    # using ClientThread() class for new thread
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)

# wait until created thread terminates
# for t in threads:
#     t.join()
