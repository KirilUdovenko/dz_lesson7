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
    return surname_dict["name"].split()[-1]


data_sort_by_surname = sorted(some_data, key=lambda surname_dict: surname_dict["name"].split()[-1])
print(data_sort_by_surname)


def sort_by_years(year_dict):
    year = year_dict["years"]
    return year


data_sort_by_year = re.findall(r"\d+", some_data)
print(data_sort_by_year)


def sort_by_len_text(person_dict):
    return len(person_dict["text"].split())


data_math_sort_by_len_text = sorted(some_data, key=lambda person_dict: len(person_dict["text"].split()))
print(data_math_sort_by_len_text)
