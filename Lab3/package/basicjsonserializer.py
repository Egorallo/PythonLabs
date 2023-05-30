from constants.formats import JSON
from constants.constants import BOOL_TYPES, PRIMITIVES, TYPE_MAPPING
from funcs.funcs import get_key, to_number, get_items


class JSONSerializer:

    def dumps(self, obj):
        if type(obj) == str:
            return f'"{obj}"'

        if type(obj) in (int, float, complex):
            return str(obj)

        if type(obj) in [bool, type(None)]:
            return BOOL_TYPES[obj]

        return JSON.format(
            type=type(obj) if type(obj) in TYPE_MAPPING.values() else object,
            id=id(obj),
            items=self.__load_to_json(get_items(obj))
        )

    def loads(self, load_from: str):
        if not len(load_from):
            return

        if load_from == ' ':
            return ...
        if load_from.startswith('"'):
            return load_from.strip('"')
        if load_from in BOOL_TYPES.values():
            return get_key(load_from, BOOL_TYPES)
        if to_number(load_from) is not None:
            return to_number(load_from)





    def __load_to_json(self, obj: dict):
        json_format = ""

        for k, v in obj.items():
            if type(v) in PRIMITIVES:

                json_format += f"\t{self.dumps(k)}: {self.dumps(v)},\n"
                continue

            json_format += f"\t{self.dumps(k)}: {{\n"

            for line in self.dumps(v).split("\n")[1:]:
                json_format += f"\t{line}\n"

        return json_format
