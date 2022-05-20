import datetime

current_date = datetime.datetime.now()

name = input("Please enter your name ").capitalize()
age = input(f"Hello {name} how old are ? ")
month = input(f"{name} what month were you born? ")
birth_year = int(current_date.year) - int(age)







# if current_date.month < int(month):
#     birth_year -= 1
# else:
#     birth_year
#
# print(f"{name} you were born in {int(birth_year)}")

