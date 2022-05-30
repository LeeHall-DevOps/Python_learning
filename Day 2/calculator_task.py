
num1 = int(input("enter number "))
math_sign = int(input("Enter math sign (+, -, *, / ) "))
num2 = input("Enter second number ")

def add(num1, num2):
    return  num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiple(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if math_sign == '+':
    print(add(num1, num2))
elif math_sign == '-':
    print(subtract(num1, num2))
elif math_sign == '*':
    print(multiple(num1, num2))
elif math_sign == '/':
    print(divide(num1, num2))
else:
    print("Error, math symbols only")