import json


def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data


filenames = "data.json"
some_data = read_json(filenames)
print(some_data)


def sort_by_surname(surname_dict):
    return surname_dict["name"].split()


data_surname = read_json("data.json")
data_sort_by_surname = sorted(data_surname, key=lambda surname_dict: surname_dict.get("name")[-1])
print(data_sort_by_surname)


def sort_by_len_text(person_dict):
    return len(person_dict["text"].split())


data_math = read_json("data.json")
data_math_sort_by_len_text = sorted(data_math, key=lambda person_dict: len(person_dict["text"].split()))
print(data_math_sort_by_len_text)