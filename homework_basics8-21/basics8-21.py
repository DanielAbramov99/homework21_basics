from operator import index

student = {  # 8
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding'], }


def print_data(dict_data: dict[str, str]):
    for key, value in dict_data.items():
        print(f"{key}:{value}")
        print()


def add_hobby(dict_data: list[dict[str, str]], student_hobby: str):
    if not student_hobby in dict_data["hobbies"]:
        dict_data["hobbies"].append(student_hobby)
    return dict_data


def delete_hobby(dict_data: list[dict[str, str]], student_hobby: str):
    if student_hobby in dict_data["hobbies"]:
        dict_data["hobbies"].remove(student_hobby)
    return dict_data


student.setdefault("family_name", "Jonson")

print_data(student, )
add_hobby(student, "MMA")
print_data(student)
delete_hobby(student, "games")
print_data(student)

matrix = [1, 2], [3, 4], [5, 6]  # 9


def matrix_rows(matrix_list: list[int]):
    for row in matrix_list:
        for number in row:
            (print(number, end=" "))


matrix_rows(matrix)

print()

matrix2 = [0, 1, 1], [0, 1, 0], [1, 0, 0]


def zeroes_counter(matrix2_list: list[int], counter: int = 0):  # 10
    for row in matrix2_list:
        for number in row:
            if number == 0:
                counter += 1
    print(f"the amount of zeroes in this list is {counter}")


zeroes_counter(matrix2)

numbers_list = [4, 2, 34, 4, 1, 12, 1, 4]


def duplicates_list(number_lst: list[int]):  # 11
    only_duplicates: list[int] = []
    for number in number_lst:
        if number_lst.count(number) > 1 and not number in only_duplicates:
            only_duplicates.append(number)
    print(only_duplicates)


duplicates_list(numbers_list)


def reversed_list(lst: list[any]):  # 12
    print(lst[::-1])


reversed_list([1, 2, 3, 4, 5, 6, 7, 8])


def sum_lists(lst1: list[int], lst2: list[int]):  # 13
    combined_lst: list[int] = []
    for index in range(len(lst1)):
        number_sum = lst1[index] + lst2[index]
        combined_lst.append(number_sum)
    print(combined_lst)


sum_lists([2, 4, 8], [2, 4, 8])


def palindrome_or_not(str1: str, str2: str):  # 14
    if str1.lower() == str1.lower()[::-1]:
        print(f"the first string is palindrome? {True}")
    else:
        print(f"the first string is palindrome? {False}")
    if str2.lower() == str2.lower()[::-1]:
        print(f"the second string is palindrome? {True}")
    else:
        print(f"the second string is palindrome? {False}")


palindrome_or_not("Dad", "Sad")

counter1: int = 1  # 15

while counter1 < 100:
    print(counter1, end=" ")
    counter1 *= 2
print()

counter2: int = 900_000  # 16

while counter2 > 50:
    print(counter2, end=" ")
    counter2 //= 2
print()


def string_duplicates(str_lst: list[str]):  # 17
    duplicates: list[str] = []
    unique_duplicates: list[str] = []
    x = 0

    while x < len(str_lst):
        y = x + 1
        while y < len(str_lst):
            if str_lst[x] == str_lst[y] and str_lst[x] not in duplicates:
                duplicates.append(str_lst[x])
            y += 1
        x += 1

    z = 0
    while z < len(duplicates):
        unique_duplicates.append(str_lst[z])
        z += 1
    print(unique_duplicates)


string_duplicates(["red", "yellow", "red", "black", "white", "yellow"])


def no_duplicate_str(str_lst: list[str]):  # 18
    duplicate_strings: list[str] = []
    word: int = 0
    duplicate_strings.append(str_lst[0])
    while word < len(str_lst):
        if word >= 1 and str_lst[word] not in duplicate_strings:
            duplicate_strings.append(str_lst[word])
        word += 1
    print(duplicate_strings)


no_duplicate_str(["red", "red", "yellow", "red", "black", "white", "yellow"])


def no_duplicate_str_no_pete(str_lst: list[str]):  # 19
    duplicate_strings: list[str] = []
    word: int = 0
    duplicate_strings.append(str_lst[0])
    while word < len(str_lst):
        if word >= 1 and str_lst[word] not in duplicate_strings and str_lst[word] != "pete":
            duplicate_strings.append(str_lst[word])
        word += 1
    print(duplicate_strings)


no_duplicate_str_no_pete(["red", "red", "yellow", "red", "black", "pete", "white", "yellow"])

bool_lst: list[bool] = [True, False, True, False, True, False]  # 20
index: int = 1
value: int = -1
while index < len(bool_lst):
    if bool_lst[index] == bool_lst[index - 1]:
        value = index
    index += 1
print(value)

sentinel = False  # 21 קוד לא יפה לעין אני יודע אבל עובד
while True:
    if sentinel:
        break
    full_name_input: str = str(input("enter your full name:"))
    if len(full_name_input.split()) != 2:
        print("the name input is not legal, please enter your first and last name")
    else:
        while True:
            if sentinel:
                break
            age_input: int = int(input("enter your age 1-130:"))
            if not 1 <= age_input <= 130:
                print("the age is not in range, please try again")
                continue
            else:
                while True:
                    if sentinel:
                        break
                    email_input: str = str(input("enter your email address with @:"))
                    if not "@" in email_input:
                        print("email is missing @, please try again")

                    else:
                        print(
                            f"your full name is {full_name_input}, you are {age_input} years old and your email is {email_input}")
                        sentinel = True
                        break
