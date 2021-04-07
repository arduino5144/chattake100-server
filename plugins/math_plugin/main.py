import api.v1
class MathPlugin:
    def add_numbers(*args):
        print(args)
        return args[0]+args[1]
    commands = {
        "ADD": add_numbers
    }