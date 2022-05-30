import datetime

date = datetime.datetime.now()
stored_email = "lhall@spartaglobal.com"
stored_password = "123456"

user_prompt = True
while user_prompt:
    user_email = input(f"Please enter your email ").lower()
    user_password = input(f"Please enter your password:  ")

    if user_email == stored_email   and user_password == stored_password :
        user_prompt = False
    else:
        print(f"Please enter correct information")


print(f"Welcome ")
print(f"You have logged in on {date.strftime('%a')} {date.strftime('%d')} {date.strftime('%b')} {date.strftime('%Y')} ")
