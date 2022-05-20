name = input("what is your name? ").capitalize()
height = input(f"How tall are you {name}? ")
favorite_color = input(f"What is your favorite color {name}? ")
secret_spirit_animal = input(f"What is your secret spirit animal {name}? ")

print(f"Welcome {name} to the guessing game")
print(f"{name} is {int(height)} tall and {name}'s favorite colour is {favorite_color}")
print(f"First letter of the secret spirit animal '{secret_spirit_animal[:1]}' and last letter of the secret spirit animal '{secret_spirit_animal[-1:]}'")
print(f"The number of letters are {len(secret_spirit_animal)}")

user_guess = input(f"Please guess the secret spirit animal ")

if user_guess == secret_spirit_animal:
    print("OMG how did you know?! :D")
else:
    print("Try Again!")