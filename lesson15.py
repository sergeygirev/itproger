#context manager (`with ... as`)

# file = open('text.txt', 'r')
# file.read()
# file.close()

# try:
#     file = open('text.txt', 'r')
#     file.read()
#     # file.close()
# except FileNotFoundError:
#     print("File not found")
# finally:
#     file.close()

# try:
#     with open('text.txt', 'r', encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('File not found')

#homework from chatgpt
# name = input("Введите имя: ")
# with open("users.txt", "w", encoding="utf-8") as file:
#     print(name, file=file)
# with open("users.txt", "r", encoding="utf-8") as file:
#     print("Список пользователей:")
#     for line in file:
#         print('-', line.strip())

# food1 = input('First food?')
# food2 = input('Second food?')
# food3 = input('Third food?')
# with open('foodfile.txt', 'w') as file:
#     print(food1, file=file)
#     print(food2, file=file)
#     print(food3, file=file)
# with open('foodfile.txt', 'r') as file:
#     print('Menu:')
#     for line in file:
#         print('-', line.strip())

# with open('foodfile.txt', 'w', encoding='utf-8') as file:
#     while True:
#         food = input("Введите блюдо (или 'stop' для выхода): ")
#         if food.lower() == 'stop':
#             break
#         print(food, file=file)
#
# with open('foodfile.txt', 'r', encoding='utf-8') as file:
#     print("Ваше меню:")
#     for line in file:
#         print("-", line.strip())

# name = input('What is your name?:')
# with open('names.txt', 'r', encoding='utf-8') as file:
#     users = [line.strip() for line in file]
# if name in users:
#         print('Name is already here')
# else:
#     with open('names.txt', 'a', encoding='utf-8') as file:
#         print(name, file=file)
#     print('Name is now here')
# with open('names.txt', 'r', encoding='utf-8') as file:
#     print('Names:')
#     for line in file:
#         print("-", line.strip())