from socket import *
import random

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverPort = 6789
serverSocket.bind(('', serverPort))

while True:
    print('The server is running')
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    
    if rand < 4:
        continue
    
    serverSocket.sendto(message, address)

