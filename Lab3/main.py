from package.basicjsonserializer import JSONSerializer

def main():
    class A:
        def check(self):
            return "wowzers"

    a = A()
    ser = JSONSerializer()
    dumped = ser.dumps(a)
    print(dumped)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
