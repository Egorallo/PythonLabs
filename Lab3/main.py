from package.basicjsonserializer import JSONSerializer
from package.basicxmlserializer import XMLSerializer
import math
import argparse


def main():
    # class B:
    #     pass
    #
    # class A:
    #     def __init__(self):
    #         self.name = 'joe'
    #     def check(self):
    #         return
    #     @staticmethod
    #     def meth():
    #         print("nah", )
    #
    # class C(A,B):
    #
    #
    #
    #     def check(self):
    #         return 12
    #
    # c = C
    # c.meth()
    #
    #
    # ser = XMLSerializer()
    # dumped = ser.dumps(C)
    # loaded = ser.loads(dumped)
    # # print(dumped)
    # if < param and func -> int, return result+3
    # def decorator(param):
    #     def upper(func):
    #         def wrapper(*args, **kwargs):
    #             return func(args[0]) + 3 if (len(args) + len(kwargs) < param and type(func(args[0])) == int) else func(
    #                 args[0])
    #
    #         return wrapper
    #
    #     return upper
    #
    # def decorator2(func):
    #     def wrapper(*args, **kwargs):
    #         return func()
    #
    #     return wrapper
    #
    # @decorator2
    # def somefunc():
    #     pass
    #
    # @decorator(3)
    # def func(*args, **kwargs):
    #     return args[0]
    #
    # print(func(2, 3, a=5))

    ser = JSONSerializer()
    a = None
    print(ser.dumps(a))

    parser = argparse.ArgumentParser()
    parser.add_argument("read_from")
    parser.add_argument("write_to")
    parser.add_argument("format_from")
    parser.add_argument("format_to")

    args = parser.parse_args()

    read_from, write_to, format_from, format_to = args.read_from, args.write_to, \
        args.format_from, args.format_to

    with open(read_from, 'r') as file, \
            open(write_to, 'w+') as file_to:

        format_from: JSONSerializer | XMLSerializer = JSONSerializer() if format_from == "json" else XMLSerializer()
        format_to: JSONSerializer | XMLSerializer = JSONSerializer() if format_to == "json" else XMLSerializer()

        format_to.dump(format_from.load(file), file_to)

    # ser = JSONSerializer()
    # a = {10: "why", 20: "when", 30: "where"}
    # print(ser.dumps(a))

if __name__ == '__main__':
    main()
