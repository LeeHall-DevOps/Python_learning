import json

car_data = {"name": "tesla", "engine": "electric"}

with open("new_json_file.json") as jsonfile:
    # load takes the json format and puts it into python format
    car = json.load(jsonfile)
    print(type(car))
    print(car['name'])
    print(car['engine'])



# writing to json
# with open('new_json_file.json', 'w') as jsonfile:
#     json.dump(car_data, jsonfile)


# car_data_json_string = json.dumps(car_data)
# #print(type(car_data))
# print(car_data_json_string)
# print(type(car_data_json_string))
