from socket import socket, gethostname
from pathlib import Path

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

class SocketConnect:
    def __init__(self, host, port):
        self.socket = socket()
        self.host = host
        self.port = port


    def connect_to_server(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Connected to host: {HOST} . . . ")

    def receive_video(self):
        n=0
        connection, addr = self.socket.accept()

        print("Starting to read bytes")
        buffer = connection.recv(1024)

        with open('media/scheduled_video.mp4', "wb+") as video:
            n += 1
            i = 0
            while buffer:
                video.write(buffer)
                print(f"buffer {i}")
                i += 1
                buffer = connection.recv(1024)

        print("done reading bytes")
        connection.close()