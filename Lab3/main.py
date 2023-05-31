from package.basicjsonserializer import JSONSerializer
from package.basicxmlserializer import XMLSerializer
def main():
    class A:
        def check(self):
            return "wowzers"

    a = A()
    ser = XMLSerializer()
    dumped = ser.dumps(a)
    loaded = ser.loads(dumped)
    print(dumped)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
