import socket
import json


class ClientConnection(object):
    def __init__(self, host, port, *args, **kw):
        self.host = host
        self.port = port

    def get_data(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((self.host, self.port))

        tm = s.recv(10 * 1024)

        s.close()

        return tm.decode('utf-8')
