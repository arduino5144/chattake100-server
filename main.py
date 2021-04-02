import socket
from _thread import *
from plugins import datetime_command

# datetime_command_instance = datetime_command

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        encoded_data = connection.recv(2048)
        data = encoded_data.decode('utf-8')
        words_received = data.split()
        response = 'Server message: ' + data
        if not data:
            break
        # connection.sendall(str.encode(response))

        print(words_received)
        result = datetime_command.commands[words_received[0]]()
        connection.send(str.encode(result))
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
