import json
import re


def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data


filenames = "data.json"
some_data = read_json(filenames)
print(some_data)


def sort_by_surname(surname_dict):
    name = surname_dict["name"][-1]
    return name


data_surname = read_json(filenames)
data_sort_by_surname = sorted(data_surname, key=lambda surname_dict: len(surname_dict["name"].split()))
print(data_sort_by_surname)


# def sort_by_years(year_dict):
#     year = year_dict["years"]
#     return year
#
#
# data_year = read_json(filenames)
# data_sort_by_year = re.findall(r"[0-9]+", data_year)
# print(data_sort_by_year)


def sort_by_len_text(person_dict):
    return len(person_dict["text"].split())


data_math = read_json(filenames)
data_math_sort_by_len_text = sorted(data_math, key=lambda person_dict: len(person_dict["text"].split()))
print(data_math_sort_by_len_text)
