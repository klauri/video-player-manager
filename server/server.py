#!/usr/bin/python3

from socket import socket, gethostname, SHUT_WR

def connect_to_client(host, port):
    sock = socket()
    sock.connect((host, port))
    return sock


def send_video(filename, socket):
    print("Sending video..")
    with open(filename, "rb") as video:
        buffer = video.read()
        print(buffer)
        socket.sendall(buffer)

    print("Done sending..")
    socket.close()

if __name__=='__main__':
    socket = connect_to_client('127.0.0.1', 65432)

    send_video("scheduled_media/EldenRing.mp4", socket)