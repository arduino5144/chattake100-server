import api.v1


class HelloWorldPlugin(api.v1.Plugin):
    def send_hello_world(self, args, user):
        return "Hello, World!"

    def send_bananas(self, args, user):
        return "Bananas"

    commands = {
        "HELLOWORLD": send_hello_world,
        "BANANAS": send_bananas
    }