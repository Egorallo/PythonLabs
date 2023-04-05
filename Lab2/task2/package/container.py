import os
import re
import pickle


class Container:

    SAVE_PATH = os.path.relpath('data/')

    def __init__(self):
        self.__data = set()

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data: set):
        self.__data = new_data

    def add(self, keys: tuple[str]):
        self.data.update(keys)

    def remove(self, key: str):
        if key not in self.data:
            print("Couldn't find such key")
        else:
            self.data.remove(key)

    def find(self, key: str):
        if key in self.data:
            return True
        else:
            return False

    def list(self):
        return list(self.data)

    def grep(self, regex: str):
        try:
            re.compile(regex)
        except re.error:
            return []

        matched_keys = []
        for element in self.data:
            if re.search(regex, element):
                matched_keys.append(element)

        return matched_keys

    def save(self, username: str):
        path = os.path.join(self.SAVE_PATH, f"{username}.pkl")

        with open(path, 'wb+') as f:
            pickle.dump(self.data, f)

    def load(self, username: str, switch=False):
        path = os.path.join(self.SAVE_PATH, f"{username}.pkl")

        if not os.path.lexists(path):
            if switch:
                self.data = set()
            return

        with open(path, 'rb') as f:
            try:
                new_data: set = pickle.load(f)
            except pickle.UnpicklingError:
                new_data = set()

        if switch:
            self.data = new_data
        else:
            self.data.update(new_data)
