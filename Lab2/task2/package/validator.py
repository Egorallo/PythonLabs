from task2.constants.messages import TERMINAL_COMMANDS
import re


class Validator:

    @classmethod
    def validate_command(cls, input_line: str):
        try:
            possible_command = input_line.split()[0]
        except IndexError:
            return "Not a command"

        if possible_command in TERMINAL_COMMANDS.keys():
            return possible_command
        else:
            return f"{possible_command}: command not found"

    @classmethod
    def validate_username(cls):
        while True:
            username = input("Enter your username: ")
            pattern = re.compile(r'^[a-zA-Z0-9]{3,}$')

            if bool(pattern.match(username)):
                return username
            else:
                print("Username must be at least 3 characters"
                      " long and contain only numbers and/or latin letters")
