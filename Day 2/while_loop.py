# x = 0
#
# while x <= 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break
#     x += 1

user_prompt = True
# The while loop below will continue asking the user to input a
# digit. and will continue to loop until digit is entered.
while user_prompt:
    age = input("What is your age? ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide your answer in digits")

print(f"Your age is {age}")