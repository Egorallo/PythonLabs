import sys
from task2.constants.messages import TERMINAL_GREETING
from task2.package.user import User
from task2.package.validator import Validator


class Terminal:

    def __init__(self):
        self.__user: User | None = None
        self.__prompt = None

    def start_terminal(self):
        print(TERMINAL_GREETING)

        self.__user = User(Validator.validate_username())

        while True:
            try:
                self.__prompt = input(f"{self.__user.username} >> ")
                command = Validator.validate_command(self.__prompt)

                match command:
                    case "add":
                        self.add_command()
                    case "remove":
                        self.remove_command()
                    case "find":
                        self.find_command()
                    case "list":
                        self.list_command()
                    case "grep":
                        self.grep_command()
                    case "save":
                        self.save_command()
                    case "load":
                        self.load_command()
                    case "switch":
                        print("switched")
                    case _:
                        print(command)
            except KeyboardInterrupt:
                sys.exit()

    def add_command(self):
        args = Validator.validate_args(self.__prompt)
        if len(args) != 0:
            self.__user.add_keys(args)
        else:
            print("Arguments weren't provided")

    def remove_command(self):
        args = Validator.validate_args(self.__prompt)

        if len(args) == 1:
            self.__user.remove_key(args[0])
        elif len(args) == 0:
            print("Nothing to remove")
        else:
            print("One argument should be provided")

    def find_command(self):
        args = Validator.validate_args(self.__prompt)

        if len(args) != 0:
            self.__user.find_keys(args)
        else:
            print("Nothing found")

    def list_command(self):
        self.__user.list_keys()

    def grep_command(self):
        args = Validator.validate_args(self.__prompt, True)

        if len(args) != 0:
            self.__user.grep_keys(''.join(args))
        else:
            print("No matches found.")

    def save_command(self):
        self.__user.save()

    def load_command(self):
        self.__user.load()

    def switch_command(self):
        pass
