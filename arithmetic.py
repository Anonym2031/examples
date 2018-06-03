def arithmetic(number1, number2, operation):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        return number1 / number2
    else:    # if operation not +,-,*,/ then return error
        return "Error"


num1 = int(input("Num 1  -  "))  # input fist number
num2 = int(input("\nNum 2  -  "))  # input next number
opr = str(input("\nOperation - "))  # input the operation
print("\n", arithmetic(num1, num2, opr))
