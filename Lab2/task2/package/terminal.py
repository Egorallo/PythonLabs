from task2.package.user import User

class Terminal:

    def __init__(self):
        self.__user = None
        self.__prompt = None

    def start_terminal(self):
        print("$$$Terminal started$$$")

        self.__user = User(input("Enter username: "))

        while True:
            self.__prompt = input(f"{self.__user.username} >> ")
            command = self.__prompt
            match command:
                case "add":
                    print("added")
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

