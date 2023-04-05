from task2.constants.messages import TERMINAL_COMMANDS


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


