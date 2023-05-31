from package.basicjsonserializer import JSONSerializer
from package.basicxmlserializer import XMLSerializer
import math


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
    def decorator(param):
        def upper(func):
            def wrapper(*args, **kwargs):
                return func(args[0]) + 3 if (len(args) + len(kwargs) < param and type(func(args[0])) == int) else func(
                    args[0])

            return wrapper

        return upper

    def decorator2(func):
        def wrapper(*args, **kwargs):
            return func()

        return wrapper

    @decorator2
    def somefunc():
        pass

    @decorator(3)
    def func(*args, **kwargs):
        return args[0]

    print(func(2, 3, a=5))


if __name__ == '__main__':
    main()
