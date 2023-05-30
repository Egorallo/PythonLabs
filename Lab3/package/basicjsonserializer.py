from constants.formats import JSON

class JSONSerializer:

    def dumps(self, obj):
        if type(obj) == str:
            return f'"{obj}"'

        if type(obj) in (int, float, complex):
            return str(obj)

        if type(obj) in [bool, type(None)]:
            bools = {True: "True", False: "False", None: "None"}
            return bools[obj]


    def loads(self):
        """
        to be implemented
        """

