#exception handling (`try/except`)
# x = int(input('Your number: '))
# x += 5
# print(x)

# try:
#     x = int(input('Your number: '))
#     x += 5
#     print(x)
# except ValueError:
#     print('You did not enter a number.')

# x = 0
# while x == 0:
#     try:
#         x = int(input('Your number: '))
#         x += 5
#         print(x)
#     except ValueError:
#         print('Please enter a number.')

# try:
#     # x = 5 / 0
#     x = int(input())
# except ZeroDivisionError:
#     print('Delenie na nol')
# except ValueError:
#     print('Nada na nol')
# else:
#     print('Wrong')
# finally:
#     print('Feli nada')

#homework from chatgpt
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     x = a / b
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("No zero")
# else:
#     print('Result:', round(x, 2))
# finally:
#     print("Goodbye")

# try:
#     x = int(input("Enter a number: "))
#     x = x ** 2
#     print(x)
# except ValueError:
#     print("Invalid input")
# finally:
#     print("Goodbye")

# try:
#     x = int(input("Enter a number: "))
#     if x < 0:
#         print("The number cannot be negative.")
#     elif x == 0:
#         print("Zero.")
#     else:
#         print("The number is: ", x ** 2)
# except ValueError:
#     print("Invalid input.")
# finally:
#     print("The program is done.")