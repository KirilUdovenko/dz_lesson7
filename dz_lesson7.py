import json

some_data = [12, 23, 34, 45]
print(some_data)

# with open("some_data.json", "w") as file:
#     file.write(str(some_data))

with open("some_data.json", "r") as file:
    some_data = file.read()

print(some_data)

# def read_json(filename):
#     with open(filename, "r") as file:
#         some_data = json.load(file)
#         return some_data
#
#
# filename = "some_data.json"
# data = read_json(filename)
# print(data)


