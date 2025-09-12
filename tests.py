# word = int(input('Enter number: '))
# i = 0
# while i < word:
#     i += 1
#     if i % 2 == 0:
#         print(i, 'even')
#     if i % 2 > 0:
#         print(i, 'odd')
# from http.cookiejar import uppercase_escaped_char
from sys import get_coroutine_origin_tracking_depth

# n = int(input("Enter number: "))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i, 'even')
#     else:
#         print(i, 'odd')
#     i += 1


# numbers = []
# number1 = input('Press number: ')
# number2 = input('Press number: ')
# number3 = input('Press number: ')
# number4 = input('Press number: ')
# number5 = input('Press number: ')
# numbers.append(int(number1))
# numbers.append(int(number2))
# numbers.append(int(number3))
# numbers.append(int(number4))
# numbers.append(int(number5))
# print('List of numbers:', numbers)
# print('Summ:', sum(numbers))
# print('First:', numbers[0], 'Last:',numbers[-1])

# numbers = []

# for i in range(5):
#     num = int(input(f'Press number #{i+1}: '))
#     numbers.append(num)
#
# print('List of numbers:', numbers)
# print('Summ:', sum(numbers))
# print('Max:', max(numbers))
# print('Min:', min(numbers))

# book = {
#     "title": "The Vampire Diaries",
#     "author": "Smith",
#     "year": 1999,
# }
# book['pages'] = '365'
# book['year'] = 1965
# print(book)

# library = [
#     {"title": "The Vampire Diaries", "author": "Smith", "year": 1965, "pages": 365},
#     {"title": "Harry Potter", "author": "Rowling", "year": 1997, "pages": 400},
#     {"title": "War and Peace", "author": "Tolstoy", "year": 1869, "pages": 1225}
# ]
# for i in range(len(library)):
#     print(library[i]["title"], '-', library[i]["author"], '(',library[i]["year"],'),', library[i]["pages"], "pages")
# for book in library:
#     print(book["title"] + " - " + book["author"] + " (" + str(book["year"]) + "), " + str(book["pages"]) + " pages")

# students = [
#     {'name': 'Ivan', 'grades': [4, 5, 3, 5]},
#     {'name': 'Masha', 'grades': [5, 5, 5, 4]},
#     {'name': 'Dima', 'grades': [3, 4, 4, 3]}
# ]
# for student in students:
#     i = sum(student['grades']) / len(student['grades'])
#     student['status'] = i
    # if i >= 4.5:
    #         print(student['name'], '-', student['status'], '-', 'good')
    # if i >= 3.5 and i < 4.5:
    #         print(student['name'], '-', student['status'], '-', 'normal')
    # if i < 3.5:
    #         print(student['name'], '-', student['status'], '-', 'bad')
    # if i > 4.5:
    #     status = 'good'
    # elif 3.5 <= i <= 4.5:
    #     status = 'normal'
    # else:
    #     status = 'bad'
    # student['status'] = status
    # print(student['name'], '-', i, '-', student['status'])

# строка(string, str)
# word = "hello"
# print(word[0])
# print(word.upper())

# список(list)
# fruits = ["apple", "banana"]
# fruits.append("cherry")   # добавили элемент
# fruits[0] = "pear"        # заменили первый элемент
# print(fruits)  # ['pear', 'banana', 'cherry']
#
# кортеж(tuple)
# colors = ("red", "green", "blue")
# print(colors[1])   # green
# # colors[1] = "black"  # ❌ Ошибка: нельзя изменить

# словарь(dictionary, dict)
# person = {"name": "Sergey", "age": 28}
# print(person["name"])   # Sergey
# person["age"] = 29      # изменили значение
# person["city"] = "Belgrade"  # добавили новый ключ
# print(person)
# {'name': 'Sergey', 'age': 29, 'city': 'Belgrade'}

# множество(set)
# nums = {1, 2, 3, 3, 2, 1}
# print(nums)  # {1, 2, 3} — дубликаты исчезли
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)  # {1, 2, 3, 4, 5} (объединение)
# print(a & b)  # {3} (пересечение)

# text = 'football, skate, Football, chess, skate'
# hobbies = text.split(',')
# clean = [h.strip() for h in hobbies]
# lowercased = [h.lower() for h in clean]
# unique = set(lowercased)
# sorted_hobbies = sorted(unique)
# final = [h.title() for h in sorted_hobbies]
# print(final)
# print('Unique:', len(final))

# text = "football, skate, Football, chess, skate"
# hobbies = text.split(",")
# hobbies_clean = []
# for item in hobbies:
#     hobbies_clean.append(item.strip())
# hobbies_lower = []
# for item in hobbies_clean:
#     hobbies_lower.append(item.lower())
# hobbies_unique = set(hobbies_lower)
# hobbies_sorted = sorted(hobbies_unique)
# hobbies_final = []
# for item in hobbies_sorted:
#     hobbies_final.append(item.title())
# print(hobbies_final)
# print("Всего уникальных:", len(hobbies_final))