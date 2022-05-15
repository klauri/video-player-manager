from connections.Socket import SocketConnect

if __name__=='__main__':
    socket = SocketConnect('127.0.0.1', 65432)
    socket.connect_to_server()
    socket.receive_video()