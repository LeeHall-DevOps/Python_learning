list_data = [1,2,3,4,5]
embedded_list = [[1,2,3], [4,5,6]]
dict_data = {
        1: {"name": "Bronson", "money": "$0.05"},
        2: {"name": "Masha", "money": "$3.66"},
        3: {"name": "Roscoe", "money": "$1.14"}}

# for num in list_data:
#     print(num * 2)
#     print("Hello")
#     print("Testing")

"""
if you want to go through your code step by step, use F8 for break point
F9 for debug mode
"""
# for data in embedded_list:
#     print(data)
#
#     for num in data:     # nested loops
#         print(num)

# for item in dict_data.values():
#     print(item)



# for item in dict_data.values():
#     for embed_value in item:

# for items in dict_data.values()
#     print(items['money'])


# for loop with if statements
for num in list_data:
    if num == 3:
        print("I've found three")
    elif num >  3:
        print("I've gone too far")
    else:
        print("Too soon")

