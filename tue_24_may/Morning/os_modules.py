import os
import  math, datetime, sys

working_dir = os.getcwd()

# built-in functions are easily access able
type(working_dir)
len(working_dir)

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.uname())

def operating_system_info():
    print(os.cpu_count())

print(datetime.date.today())

print(sys.path)

print(math.remainder(1, 5))

print(operating_system_info())