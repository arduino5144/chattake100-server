import api.v1
import datetime

class DatetimePlugin(api.v1.Plugin):
    def send_datetime_to_user(self, args, username):
        current_datetime = str(datetime.datetime.now())
        return current_datetime

    commands = {
        "DATETIME": send_datetime_to_user
    }
