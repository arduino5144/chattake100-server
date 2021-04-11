import api.v1

class HelloWorldPlugin(api.v1.Plugin):
    def send_hello_world(self, args, username):
        return "Hello, World!"

    def send_bananas(self, args, username):
        return "Bananas"

    commands = {
        "HELLOWORLD": send_hello_world,
        "BANANAS": send_bananas
    }