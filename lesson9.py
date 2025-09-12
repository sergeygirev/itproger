# tuples

# data = (4, 6, 7, 3, 6, True, 5.6, 'Hello')
# data[1] = 5 - no
# print(data[1:3])
# print(data.count(6))
# print(len(data))

# data = (5)
# print(data)

# data = (5,)
# print(data)

# data = 5, 7, True
# print(data)

# data = (4, 6, 7, 3, 6, True, 5.6, 'Hello')
# for el in data:
#     print(el, end = ',')
# num = [5, 7, 8]
# new_data = tuple(num)
# print(new_data)

# word = ('hello world')
# print(word)

# word = tuple('hello world')
# print(word)

# homework from chat gpt
# fruits = ['apple', 'banana', 'orange']
# fruits[0] = 'banana'
# print(fruits)
# new_fruits = tuple(fruits)
# print(new_fruits)

# numbs = (1, 2, 3, 4, 5, 6, 5, 8, 9, 5)
# print(sum(numbs))
# print(max(numbs), min(numbs))
# print(numbs.count(5))

names = ["Sergey", "Dima", "Masha"]
ages = (28, 25, 30)
for i in range(len(names)):
    print(names[i], ages[i])

# names = ["Sergey", "Dima", "Masha"]
# ages = (28, 25, 30)
# cities = ("Loznica", "Novi Sad", "Moscow")
# for i in range(len(names)):
#     print(names[i], ages[i], cities[i])

# names = ["Sergey", "Dima", "Masha"]
# ages = [28, 25, 30]
# cities = ["Loznica", "Novi Sad", "Moscow"]
# new_name = input("Enter new name: ")
# new_age = int(input("Enter new age: "))
# new_city = input("Enter new city: ")
# names.append(new_name)
# ages.append(new_age)
# cities.append(new_city)
# for i in range(len(names)):
#      print(names[i], ages[i], cities[i])
# print(sum(ages)/len(ages))