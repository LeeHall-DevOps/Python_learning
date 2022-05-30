# age = 19
#
# if age > 18:
#     # Python uses indentation a block of code
#     print("You are the correct age to watch this film")
# elif age < 15:
#     print('you are not the correct age')
# else:
#     print('you are not the correct age')

film_rating = 'universal'

if film_rating.lower() == 'universal':
    print("All age groups can watch this film")
elif film_rating.lower() == 'pg':
    print('General viewing, parental guidance for children')
elif film_rating.lower() == '12' or film_rating == '12a':
    print('Film classified 12A and video works classied 12 contain material that may not be suited for children')
