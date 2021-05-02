import api.v1


class HelloWorldPlugin(api.v1.Plugin):
    def send_hello_world(args, user):
        return "Hello, World!"

    def send_bananas(args, user):
        return "Bananas"

    commands = {
        "HELLOWORLD": send_hello_world,
        "BANANAS": send_bananas
    }