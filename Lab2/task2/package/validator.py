class Validator:

    @classmethod
    def validate_command(cls, input_line: str):
        possible_command = input_line.split()[0]

        if possible_command == "":
            return "Command not found"

        return possible_command
