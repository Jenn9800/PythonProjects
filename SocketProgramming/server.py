import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pars = ('127.0.0.1', 7864) # you can change the server port to whatever you want
s.bind(pars)

s.listen(5)


def serveClient(clientsocket, address):
    # we need a loop to continuously receive messages from the client
    while True:
        # then receive at most 1024 bytes message and store these bytes in a variable named 'data'
        # you can set the buffer size to any value you like
        data = clientsocket.recv(1024)
        print("from client", data)

        # if the received data is not empty, then we send something back by using send() function
        if data:
            clientsocket.send(b'response')

        # we need some condition to terminate the socket
        # lets see if the client sends some termination message to the server
        # if so, then the server close the socket
        if data == b'close':
            clientsocket.close()
            break


while True:
    # accept a new client and get it's information
    (clientsocket, address) = s.accept()

    # create a new thread to serve this new client
    # after the thread is created, it will start to execute 'target' function with arguments 'args'
    threading.Thread(target=serveClient, args=(clientsocket, address)).start()