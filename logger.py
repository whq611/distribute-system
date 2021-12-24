import socket
import sys
import threading
import time


class Node:
    def __init__(self):
        self.data = []

    def addData(self, dataIn):
        if len(self.data) == 0:
            self.data.append(dataIn[2:-3].split(' '))
            print(self.data[-1][1] + ' - ' + self.data[-1][0] + " connected")
            self.data[-1].append(time.time())
            self.data[-1].append(len(dataIn))
        else:
            self.data.append(dataIn[2:-3].split(' '))
            print(self.data[-1][1] + ' - ' + self.data[-1][0] + " " + self.data[-1][2])
            self.data[-1].append(time.time())
            self.data[-1].append(len(dataIn))

def nodeThread(conn, addr):
    node = Node()

    with conn:
        while True:
            data = conn.recv(1024)
            if not data: break
            node.addData(repr(data))
        conn.close()
    print(node.data[-1][1] + ' - ' + node.data[-1][0] + " disconnected")
    
    with open("s1/" + node.data[-1][0] + ".txt", "a") as ab:
        for i in node.data:
            for j in i:
                ab.write(str(j) + " ")
            ab.write('\n')
        ab.close()
    return

def main():
    HOST = ''
    PORT = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=nodeThread, args=(conn, addr))
        t.start()

if __name__ == "__main__":
    main()

    

