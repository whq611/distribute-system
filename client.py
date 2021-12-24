import socket
import sys

if len(sys.argv) > 3:
    NAME = str(sys.argv[1])
    HOST = str(sys.argv[2])
    PORT = int(sys.argv[3])


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    for line in sys.stdin:
        print(line, end='')
        s.sendall(str.encode(NAME + ' ' + line))