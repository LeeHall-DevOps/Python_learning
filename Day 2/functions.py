#from typing import Dict, List

# functions allow the dev to reuse the code in the function,
# # functions are better small
# def print_something(print_string):
#     print(print_string)
#
# print_something("Hello world")

# def greeting(name):
#     print("hello, my name is " + name)
#     greeting("Lee")

# def addition(int1, int2):
#     return int1 + int2

# print(addition(2, 2))
#
# x = 10
# x = (addition(2, 2))

# * means we can pass as many parameters as we want
# def multi_args(*multiargs):
#     print(type(multiargs))
#
#     for arg in multiargs
#         print(arg)
#
#         multi_args(1,2,3,4,5,6, 100, 2020)
#
# # good practice (name: str)
# def greeting(name: str):
#     print("Hello, my name is " + name)
#
# greeting(24601)

# def division(denom: int, num: int) -> float:
#     return denom / num
#
# def subtraction(int1: int =  5, int2 =  2) -> int:
#     return int1 - int2
#
# a: int = 10
# b: int = 7
#
# print(subtraction(10, 7))

names = List[str] = ['Tom', 'Dick', 'Harry']
options = Dict[str, bool] =   {"subtitles": True, "colorblind_mode": True }


"""
Make sure to always return you functions
Make functions smalls
Make use of comments in your code 
"""