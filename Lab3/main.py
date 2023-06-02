from package.basicjsonserializer import JSONSerializer
from package.basicxmlserializer import XMLSerializer
import math
import argparse


def main():
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
    # # def decorator2(func):
    # #     def wrapper(*args, **kwargs):
    # #         return func
    # #
    # #     return wrapper
    #
    # #
    # # @decorator2
    # # def somefunc(n):
    # #     print("printing from wrapper")
    #
    # @decorator(3)
    # def func(*args, **kwargs):
    #     return args[0]
    #
    # f = decorator(3)
    # func = f(func)
    # generator = (i for i in range(30))
    # for i in generator:
    #     print(next(generator))
    # def fib(n):
    #     cur = 0
    #     prev = 1
    #     for i in range(n):
    #         yield cur
    #         cur,prev = cur+prev, cur
    #
    # gen = fib(9)
    # def fib2():
    #     for i in [1,2,3] :
    #         yield i
    # def fib3():
    #     for i in [30,40,50]:
    #         yield i
    # def foo():
    #     yield from fib2()
    #     yield from fib3()
    #
    # def decor(n):
    #     def upper(func):
    #         def wrapper(*args):
    #             try:
    #                 int == type(sum(args)) and len(args) > n
    #             except:
    #                 raise Exception("Expected int, found other.")
    #             return func(*args)
    #         return wrapper
    #     return upper
    #
    # @decor(4)
    # def myfunc(*args):
    #     return sum(args)
    #
    # print(myfunc(1,2,"cock",4,5))



    # parser = argparse.ArgumentParser()
    # parser.add_argument("read_from")
    # parser.add_argument("write_to")
    # parser.add_argument("format_from")
    # parser.add_argument("format_to")
    #
    # args = parser.parse_args()
    #
    # read_from, write_to, format_from, format_to = args.read_from, args.write_to, \
    #     args.format_from, args.format_to
    #
    # with open(read_from, 'r') as file, \
    #         open(write_to, 'w+') as file_to:
    #
    #     format_from: JSONSerializer | XMLSerializer = JSONSerializer() if format_from == "json" else XMLSerializer()
    #     format_to: JSONSerializer | XMLSerializer = JSONSerializer() if format_to == "json" else XMLSerializer()
    #
    #     format_to.dump(format_from.load(file), file_to)

    # ser = JSONSerializer()
    # a = {10: "why", 20: "when", 30: "where"}
    # print(ser.dumps(a))

    class Manager:
        def __init__(self, v: list):
            self.v = v

        def __enter__(self):
            print("Hello")
            self.temp = self.v[:]
            return self.temp

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is None:
                self.v[:] = self.temp
                print("Bye")

            return True


    manager = Manager([1,2,3])
    with manager as man:
        print(man)
        a = 5/0
        man.append(25)
        print(man)



if __name__ == '__main__':
    main()
