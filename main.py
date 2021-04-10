import socket
from _thread import *
import plugins

list_of_classes = [
    plugins.datetime_command.DatetimePlugin,
    plugins.hello_world_command.HelloWorldPlugin,
    plugins.math_plugin.MathPlugin
]

list_of_instances = list()
dict_of_things = dict()

for cls in list_of_classes:
    list_of_instances.append(cls())
    for command in cls().commands:
        dict_of_things[command] = cls().commands.get(command)
        print(command)
print(dict_of_things)



# list_of_instances = [cls() for cls in list_of_classes]

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
    username = ""
    print()
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
        result = dict_of_things[words_received[0]](words_received)
        connection.send(str.encode(str(result)))
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    # ThreadCount += 1
    # print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
