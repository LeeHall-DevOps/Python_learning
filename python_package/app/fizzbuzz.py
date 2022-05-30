def fizzbuzz():
    fizz = int(input("Please enter number for Fizz: "))
    buzz = int(input("Please enter number for Buzz: "))
    for i in range(1, 101):
        if i % fizz == 0 and i % buzz == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()