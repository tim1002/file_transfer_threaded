# client file

import socket

# declaring global vars for socket objects
TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

with open('received_file', 'wb') as f:
    print('file opened')

    while True:
        print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        print(data)

        if not data:
            f.close()
            print('file close()')
            break

        # write data to a file
        f.write(data)

print('successfully got the file')
s.close()
print('connection closed')
