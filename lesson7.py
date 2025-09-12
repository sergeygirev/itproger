# # lists and their methods
# numbs = [1, 2, 3, 4, 5, 6, 7, True, 'Hello', 4.7, [1, 2, 3]]
# numbs[2] = 230
# numbs[7] = 1
# numbs[-1].reverse()
# numbs.pop(-1)
# print(numbs[-1][2])

# numbers = [5, 2, 7]
# numbers[3]=100
# numbers.append(100)
# numbers.insert(1, True)
# b = [5, 6, 8]
# numbers.extend(b)
# numbers.sort()
# numbers.reverse()
# numbers.pop()
# numbers.remove(True)
# numbers.clear()
# print(numbers.count(6))
# print(len(numbers))
# print(numbers)

# numbs = [5, 2, 7, '50', False]
# for el in numbs:
#     el *= 2
#     print(el)

# n = int(input('Enter length: '))
# user_list = []
# i = 0
# while i < n:
#     string = 'Enter element #' + str(i+1) + ': '
#     user_list.append(input(string))
#     i += 1
# print(user_list)

#homework from chatgpt
# fruits = []
# fruits1 = input('Fruit #1: ')
# fruits2 = input('Fruit #2: ')
# fruits3 = input('Fruit #3: ')
# fruits.append(fruits1)
# fruits.append(fruits2)
# fruits.append(fruits3)
# print('Your fav friuts:', fruits)

# numbers = []
# number1 = input('Press number: ')
# number2 = input('Press number: ')
# number3 = input('Press number: ')
# numbers.append(int(number1))
# numbers.append(int(number2))
# numbers.append(int(number3))
# print('List of numbers:', numbers)
# print('Summ:', sum(numbers))

# numbers = []
# for i in range(3):
#     num = int(input(f'Press number #{i+1}: '))
#     numbers.append(num)
# print('List of numbers:', numbers)
# print('Summ:', sum(numbers))

word = input("Enter: ")
word.split()
print(len(word))
print(word[0], word[-1])
print(word[::-1])