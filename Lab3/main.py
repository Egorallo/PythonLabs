from package.basicjsonserializer import JSONSerializer

def main():
    someStr = "await"
    someNum = 4.12
    someBool = False
    ser = JSONSerializer()
    dumped = ser.dumps(someBool)
    print(dumped)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
