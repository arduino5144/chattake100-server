import socket
from _thread import *
import plugins
import users

list_of_classes = [
    plugins.DatetimePlugin,
    plugins.HelloWorldPlugin,
    plugins.MathPlugin,
    plugins.NameReminderPlugin
]

list_of_instances = list()
dict_of_things = dict()

for cls in list_of_classes:
    list_of_instances.append(cls())
    for command in cls().commands:
        dict_of_things[command] = cls().commands.get(command)
        print(command)
print(dict_of_things)

def receive_data(connection):
    encoded_data = connection.recv(2048)
    data = encoded_data.decode('utf-8')
    words_received = data.split()
    if not data:
        raise Exception
    return words_received

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
    words_received = receive_data(connection)
    print(words_received)
    user = users.get_user(words_received[1], words_received[2])
    print(user)
    if user is None:
        connection.send(str.encode("Incorrect username or password"))
        print("A user failed to connect")
        connection.close()
    else:
        connection.send(str.encode("Hi, " + user.name + "!"))
        print("A user could successfully connect")
    connection.send(str.encode('Server is working:'))

    while True:
        try:
            words_received = receive_data(connection)
        except:
            break
        print(words_received)
        result = dict_of_things[words_received[0]](args=words_received, user=user)
        connection.send(str.encode(str(result)))
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    # ThreadCount += 1
    # print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
