from calculation import calc_func


print("Hello world")

try:
    value1 = int(input("Enter the first value..\n"))
    op = input("Enter the operation required..\n")
    value2 = int(input("Enter the second value..\n"))

    print(f"Output: {calc_func(value1, value2, op)}")
except Exception as exception:
    print(exception.args)
