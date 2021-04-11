import api.v1


class NameReminderPlugin(api.v1.Plugin):
    def send_name(self, args, user):
        return user.name

    commands = {
        "WHATISMYUSERNAME": send_name
    }