from calculation import calc_func
from random import randint

print("Hello world")

try:
    value1 = int(input("Enter the first value..\n"))
    op = input("Enter the operation required..\n")
    value2 = int(input("Enter the second value..\n"))

    print(f"Output: {calc_func(value1, value2, op)}")

except Exception as exception:
    print(exception.args)

primaryList = [randint(1, 10) for i in range(10)]
print(f"Primary list: {primaryList}")
finList = [i for i in primaryList if i % 2 == 0]
print(f"Final list with even numbers: {finList}")
