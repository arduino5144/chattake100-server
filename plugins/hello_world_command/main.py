import api.v1

class HelloWorldPlugin(api.v1.Plugin):
    def send_hello_world():
        return "Hello, World!"

    commands = {
        "HELLOWORLD": send_hello_world
    }