# sets (`set`, `frozenset`)
# data = set('hello')
# print(data)
# data = {5, 7, 4, 3, 5}
# data.add(32)
# data.update(['32', True, 4, 6])
# data.remove(True)
# data.pop()
# data.clear()
# print(data)

# nums = [5, 7, 3, 5, 5]
# new_nums = set(nums)
# print(new_nums)

# new_data = frozenset([5, 7, 4, '32', True, 4, 6, 5, 7, 4, 3, 5])
# print(new_data)

#homework from chatgpt
# group1 = ["Ivan", "Masha", "Sergey", "Dima", "Ivan"]
# group2 = ["Dima", "Olga", "Sergey", "Masha", "Anna"]
# group1set = set(group1)
# group2set = set(group2)
# print(group1set)
# print(group2set)
# print(group1set | group2set)
# print(group1set & group2set)
# print(group1set - group2set)

# math = {"Ivan", "Sergey", "Masha", "Dima", "Anna"}
# physics = {"Olga", "Dima", "Sergey", "Anna", "Petr"}
# print(math & physics)
# print(math - physics)
# print(physics - math)
# print(math | physics)

# math = {"Ivan", "Sergey", "Masha", "Dima", "Anna"}
# physics = {"Olga", "Dima", "Sergey", "Anna", "Petr"}
# # math1 = (math - physics)
# physics1 = (physics - math)
# print(math1 | physics1)
# print(math ^ physics)