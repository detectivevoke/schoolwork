class Calc:

    def add(self,num1, num2):
        return int(num1) + int(num2)

    def subtract(self,num1, num2):
        return int(num1) - int(num2)

    def divide(self,num1, num2):
        return int(num1) / int(num2)

    def multiply(self,num1, num2):
        return int(num1) * int(num2)


while True:
    calculator = Calc()
    op = input("Enter operation (x, /, +, - ): ")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(num1, num2)
    if op.lower() == "x":
        answer = calculator.multiply(num1, num2)
        print("Your answer is {}!".format(answer))
    elif op.lower() == "/":
        print("Your answer is {}!".format(calculator.divide(num1, num2)))
    elif op.lower() == "+":
        print("Your answer is {}".format(calculator.add(num1,num2)))
    elif op.lower() == "-":
        print("Your answer is {}".format(calculator.subtract(num1,num2)))
    else:
        print("You need to select a correct operation!")
        pass
    