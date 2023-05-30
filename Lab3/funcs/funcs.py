from types import FunctionType, MethodType, CodeType, ModuleType, \
    BuiltinMethodType, BuiltinFunctionType, CellType, GeneratorType
from typing import Any, Collection, Iterable

from constants.constants import IGNORED_FIELDS, IGNORED_FIELD_TYPES

def get_key(value, obj: dict) -> int:
    return [key for key in obj if obj[key] == value][0]

def to_number(s: str) -> int | float | complex | None:
    for num_type in (int, float, complex):
        try:
            return num_type(s)
        except (ValueError, TypeError):
            pass

def get_items(obj) -> dict[str, Any]:
    if isinstance(obj, (BuiltinFunctionType, BuiltinMethodType)):
        return {}

    if isinstance(obj, dict):
        return obj

    elif isinstance(obj, Collection):
        return dict(enumerate(obj))

    elif isinstance(obj, CodeType):
        return {
            "argcount": obj.co_argcount,
            "posonlyargcount": obj.co_posonlyargcount,
            "kwonlyargcount": obj.co_kwonlyargcount,
            "nlocals": obj.co_nlocals,
            "stacksize": obj.co_stacksize,
            "flags": obj.co_flags,
            "code": obj.co_code,
            "consts": obj.co_consts,
            "names": obj.co_names,
            "varnames": obj.co_varnames,
            "filename": obj.co_filename,
            "name": obj.co_name,
            "firstlineno": obj.co_firstlineno,
            "lnotab": obj.co_lnotab,
            "freevars": obj.co_freevars,
            "cellvars": obj.co_cellvars,
        }
    elif isinstance(obj, property):
        return {
            "getter": obj.fget,
            "setter": obj.fset,
            "deleter": obj.fdel,
        }

    elif isinstance(obj, GeneratorType):
        a = []
        for i in obj:
            a.append(i)
        return{
            "values": a
        }

    elif isinstance(obj, FunctionType):
        if obj.__closure__ and "__class__" in obj.__code__.co_freevars:
            closure = ([... for _ in obj.__closure__])
        elif obj.__closure__:
            closure = ([cell.cell_contents for cell in obj.__closure__])
        else:
            closure = None

        return {
            "argcount": obj.__code__.co_argcount,
            "posonlyargcount": obj.__code__.co_posonlyargcount,
            "kwonlyargcount": obj.__code__.co_kwonlyargcount,
            "nlocals": obj.__code__.co_nlocals,
            "stacksize": obj.__code__.co_stacksize,
            "flags": obj.__code__.co_flags,
            "code": obj.__code__.co_code,
            "consts": obj.__code__.co_consts,
            "names": obj.__code__.co_names,
            "varnames": obj.__code__.co_varnames,
            "filename": obj.__code__.co_filename,
            "name": obj.__code__.co_name,
            "firstlineno": obj.__code__.co_firstlineno,
            "lnotab": obj.__code__.co_lnotab,
            "freevars": obj.__code__.co_freevars,
            "cellvars": obj.__code__.co_cellvars,
            "globals": {
                k: obj.__globals__[k]
                for k in (
                        set(
                            k for k, v in obj.__globals__.items()
                            if isinstance(v, ModuleType)
                        ) |
                        set(obj.__globals__) &
                        set(obj.__code__.co_names) -
                        {obj.__name__}
                )
            },
            "closure": closure,
            "qualname": obj.__qualname__
        }

    elif isinstance(obj, MethodType):
        return {
            "__func__": obj.__func__,
            "__self__": obj.__self__
        }

    elif issubclass(type(obj), type):
        return {
            'name': obj.__name__,
            'mro': tuple(obj.mro()[1:-1]),
            'attrs': {
                k: v for k, v in obj.__dict__.items()
                if (
                        k not in IGNORED_FIELDS and
                        type(v) not in IGNORED_FIELD_TYPES
                )
            }
        }

    elif issubclass(type(obj), ModuleType):
        return {'name': obj.__name__}

    elif isinstance(obj, staticmethod):
        return get_items(obj.__func__)

    elif isinstance(obj, classmethod):
        return get_items(obj.__func__)

    else:
        return {
            'class': obj.__class__,
            'attrs': {
                k: v for k, v in obj.__dict__.items()
                if (
                        k not in IGNORED_FIELDS and
                        type(k) not in IGNORED_FIELD_TYPES
                )
            }
        }