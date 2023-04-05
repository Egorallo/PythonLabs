from container import Container


class User:

    def __init__(self, username: str):
        self._username = username
        self._container = Container()

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        self._username = new_username

    @property
    def container(self):
        return self._container

    def add_keys(self, keys: tuple):
        self.container.add(keys)

    def remove_key(self, key: str):
        self.container.remove(key)

    def find_keys(self, keys: tuple):
        found = []
        for key in keys:
            if self.container.find(key):
                found.append(key)

        print(found) if found else print("Couldn't find such keys")

    def list_keys(self):
        return print(self.container.list())

    def grep_keys(self, regex: str):
        print(self.container.grep(regex))

    def save(self):
        self.container.save(self.username)

    def load(self):
        pass

    def switch(self):
        pass
