from sys import exit


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

try:
    if num2 == 0:
        raise MyError("Mistake! Are you trying to divide by 0!")
    res = num1 / num2
except MyError as err:
    print(err)
else:
    print(f"Division result {num1} by {num2} =", res)