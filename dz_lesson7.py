import json

data = [
    {
        "name": "Alhazen",
        "years": "965 – 1040",
        "text": "Discovered a general method to find the sum of any integral power and hence the volume of a paraboloid; solved Alhazen's problem concerning the reflection of light from curved surfaces."
    },
    {
        "name": "Archimedes",
        "years": "287 BC – 212 BC",
        "text": "Founded the sciences of mechanics and hydrostatics, calculated pi precisely, devised the law of exponents, created new geometrical proofs, invented numerous ingenious mechanical devices and more."
    },
    {
        "name": "Daniel Bernoulli",
        "years": "1700 – 1782.",
        "text": "Discovered the Bernoulli Effect explaining how aircraft wings generate lift; formulated a kinetic theory relating particle speeds in gases to temperature; made major discoveries in the theory of risk."
    },
    {
        "name": "Leonhard Euler",
        "years": "1707 – 1783.",
        "text": "Published more mathematics than any other single mathematician, much of it groundbreaking. An astonishing fraction of the total research work in mathematics and the physical sciences between 1730 and 1780 was carried out solely by Euler."
    },
    {
        "name": "Pierre de Fermat",
        "years": "1607 – 1665.",
        "text": "Co-founded the disciplines of analytic geometry and probability theory and was a key player in the invention of calculus. There's more to Fermat than his famous last theorem."
    },
    {
        "name": "Brahmagupta",
        "years": "597 – 668.",
        "text": "Established zero as a number and defined its mathematical properties; discovered the formula for solving quadratic equations."
    },
    {
        "name": "Rene Descartes",
        "years": "1596 – 1650.",
        "text": "One of the greatest philosophers of all time; advocate of skepticism in the scientific method; creator of new mathematical ideas including the independent founding of analytical geometry. Cartesian coordinates are named in his honor."
    },
    {
        "name": "Euclid",
        "years": "325 – 270 BC.",
        "text": "Authored the Elements, the most famous and most published mathematical work in history; another great work, Optics, explained light's behavior using geometrical principles – the basis of artistic perspective, astronomical methods, and navigation methods for more than two thousand years."
    },
    {
        "name": "Fibonacci",
        "years": "c. 1170 – c. 1245.",
        "text": "The rebirth of Western mathematics: Fibonacci's Book of Calculation introduced the Indian number system, now used worldwide, to Europe."
    }
]

with open("data.json", "w") as file:
    json.dump(data, file)


# with open("data.json", "r") as file:
#     data = json.load(file)
# print(data["name"])

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
data_sort_by_surname = sorted(data_surname, key=lambda surname_dict: surname_dict["name"].split())
print(data_sort_by_surname)


def sort_by_len_text(person_dict):
    return len(person_dict["text"].split())


data_math = read_json("data.json")
data_math_sort_by_len_text = sorted(data_math, key=lambda person_dict: len(person_dict["text"].split()))
print(data_math_sort_by_len_text)
