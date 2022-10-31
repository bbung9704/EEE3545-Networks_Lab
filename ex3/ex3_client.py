from socket import *
import sys, time

argv = sys.argv
host = argv[1]
port = argv[2]
timeout = 5

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(timeout)
port = int(port)
ptime = 0

while ptime < 10:
    ptime += 1
    data = "Ping " + str(ptime) + " " + time.asctime()
    try:
        RTTb = time.time()

        # send the UDP packet with the ping message
        clientSocket.sendto(data.encode(), (host, port))
        
        # Receive the server response
        message, address = clientSocket.recvfrom(1024)
        
        RTTa = time.time()
        print("\nReply from " + address[0] + ": " + message.decode())
        RTT = RTTa - RTTb
        print("RTT: %.4f msec" %(RTT))
    except:
        print("\nRequest timed out.")
        continue

clientSocket.close()
