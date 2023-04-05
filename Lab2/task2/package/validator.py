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

    @classmethod
    def validate_args(cls, input_line: str, grep: bool = False):
        possible_args = input_line.split(maxsplit=1)

        if len(possible_args) < 2:
            return tuple()

        command = possible_args[0]

        if command not in TERMINAL_COMMANDS.keys():
            print(f"{command}: command is unknown")
            return tuple()

        if grep:
            return tuple(possible_args[1])

        args = possible_args[1].split(',')

        for i in range(len(args)):
            args[i] = args[i].strip()

        args[:] = (value for value in args if value != "")

        return tuple(args)
