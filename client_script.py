import socket
import json

host = 'localhost'
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

tm = s.recv(10 * 1024)

s.close()

print(tm.decode('utf-8'))
