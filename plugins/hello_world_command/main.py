import api.v1

class HelloWorldPlugin(api.v1.Plugin):
    def send_hello_world(args):
        return "Hello, World!"

    def send_bananas(args):
        return "Bananas"

    commands = {
        "HELLOWORLD": send_hello_world,
        "BANANAS": send_bananas
    }