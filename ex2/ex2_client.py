from socket import *
import os
import sys
import time

Host = '172.24.252.209'
Port = 6789

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((Host, Port))

message = input('요청할 파일 이름: ')
clientSocket.sendall(message.encode())

data = clientSocket.recv(4096)
data_iter = 0

os.chdir("/Users/users/Socket_Programming/ex2/client")
nowdir = os.getcwd()

with open(nowdir + "/" + message, 'wb') as f:
    try:
        while data:
            f.write(data)
            data_iter = data_iter + 1
            data = clientSocket.recv(4096)
            print('파일 %s (seq: %d) is received' %(message, data_iter))
            time.sleep(0.5)

    except Exception as ex:
        print(ex)
clientSocket.close()

# serverSocket.close()
# sys.exit()

