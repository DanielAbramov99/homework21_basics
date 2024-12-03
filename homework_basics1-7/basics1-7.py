from idlelib.editor import keynames
from operator import index
from tkinter.font import names

for num in range(12, 24 + 1):  # 1
    print(num, end=" ")
print()

for num in range(7, 31 + 1):  # 2
    print(num, end=" ") if num % 2 != 0 else None
print()

for num in range(10, -20, -1):  # 3
    print(num, end=" ") if num % 2 == 0 else None
print()

for num in range(1, 45 + 1):  # 4
    print(num, end=":FizzBuzz ") if num % 3 == 0 and num % 5 == 0 else print(num, end=":Buzz ") if num % 5 == 0 else print(
    num, end=":Fizz ") if num % 3 == 0 else None
print()


def array_sum(lst: list[int]):  # 5
    sum_result: int = 0
    for number in lst:
        sum_result += number
    return sum_result


print(array_sum([1, 13, 22, 123, 49, 34, 5, 24, 57, 45]))
print()

students: list[dict[str, any]] = [  # 6
    {"id": 332442128, "first name": "Daniel", "last name": "Abramov", "age": 222, "country": "Israel", "city": "Eilat"},
    {"id": 112442128, "first name": "Israel", "last name": "Israelov", "age": 35, "country": "Israel", "city": "Haifa"}]


def delete_property(student: list[any], properties: str):
    for key in student:
        if properties in list(key.keys()):
            del key[properties]
    print(student)


def property_only(student: list[any]):
    for value in student:
        print(value.values())


def sorted_age(student: list[any]):
    print(sorted(student, key=lambda age: age["age"]))


print(students)
(delete_property(students, "last name"))
property_only(students)
(sorted_age(students))

our_pets = [  # 7
    {
        "animal_type": "cat",
        "names": [
            "Meowzer",
            "Fluffy",
            "Kit-Cat"
        ]
    },
    {
        "animal_type": "dog",
        "names": [
            "Spot",
            "Bowser",
            "Frankie"
        ]
    }
]


def only_cat(animals: list[dict[str, str]]):
    cat = animals[0]
    key = list(cat.keys())[0]
    value = cat[key]
    print(key, value)


def animal_names(animals: list[dict[str, str]], animal_type: str):
    for animal in animals:
        if animal["animal_type"] == animal_type:
            print(animal["names"])


def add_name(animals: list[dict[str, str]], animal_name: str):
    for animal in animals:
        if not animal_name in animal["names"]:
            animal["names"].append(animal_name)
    print(animals)


only_cat(our_pets)
animal_names(our_pets, "dog")
add_name(our_pets, "Sam")
