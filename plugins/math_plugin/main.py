import api.v1
class MathPlugin:
    def add_numbers(args):
        print(args)
        try:
            return int(args[1])+int(args[2])
        except:
            return "Please input integers."
    commands = {
        "ADD": add_numbers
    }