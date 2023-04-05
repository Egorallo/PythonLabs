import sys

from task2.package.user import User
from task2.package.validator import Validator


class Terminal:

    def __init__(self):
        self.__user: User | None = None
        self.__prompt = None

    def start_terminal(self):
        print("$$$Terminal started$$$")

        self.__user = User(input("Enter username: "))

        while True:
            try:
                self.__prompt = input(f"{self.__user.username} >> ")
                command = Validator.validate_command(self.__prompt)
                match command:
                    case "add":
                        self.add_command()
                    case "remove":
                        print("removed")
                    case "find":
                        print("found")
                    case "list":
                        print("listed")
                    case "grep":
                        print("grepped")
                    case "save":
                        print("saved")
                    case "load":
                        print("loaded")
                    case "switch":
                        print("switched")
                    case _:
                        print(command)
            except KeyboardInterrupt:
                sys.exit()

    def add_command(self):
        print("added")

    def remove_command(self):
        pass

    def find_command(self):
        pass

    def list_command(self):
        pass

    def grep_command(self):
        pass

    def save_command(self):
        pass

    def load_command(self):
        pass

    def switch_command(self):
        pass
