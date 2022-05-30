# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     print("File canot be found")
#     print(errmsg)
#     raise # raise highlights error message in red

def open_and_print_file(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip("\n"))

    except:
        print("file cannot be found or dictionary is incorrect,  please check the details provided")
        raise
    finally:
        print("\n execution complete")

def write_to_file(file, order_item):
    try:
        with open(file,"w") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise


write_to_file("order.txt", "lasagna")
open_and_print_file("order.txt")








#         opened_file = open(file, "r")
#         file_line_list = opened_file.readlines()
#
#         for line in file_line_list:
#             print(line.rstrip('\n'))
#
#         opened_file.close()
#     except FileNotFoundError:
#         print("File not found or directory is incorrect, please check the details provided")
#         raise
#
# open_and_print_file("order.txt")
