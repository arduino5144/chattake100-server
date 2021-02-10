import datetime
commands = {
    "DATETIME": "plugins.datetime_command.send_datetime_to_user"
}
def send_datetime_to_user():
    current_datetime = str(datetime.datetime.now())
    return str.encode(current_datetime)