# dictionaries and working with them
# country = {4:3}
# print(country[4])

# country = {'code' : 'RU', 'name': 'Russia', 'popualtion': 144}
# print(country['code'])
# print(country.get('code'))

# country = dict(code='RU', name='Russia')
# print(country['code'])

# country = {'code' : 'RU', 'name': 'Russia', 'popualtion': 144}
# print(country.items())
# for key, value in country.items():
#     print(key, '-', value)

# country = {'code' : 'RU', 'name': 'Russia', 'popualtion': 144}
# country.clear()
# country.pop('code')
# country.popitem()
# print(country.keys())
# print(country.values())
# print(country.items())
# country['code'] = 'Region'
# print(country)

# person = {
#     'user_1': {
#         'first_name': 'John',
#         'last_name': 'Marley',
#         'age': 45,
#         'address': ('Moscow City', 'Lomonosova Street', '45'),
#         'grades': {'math': 5, 'physics': 3, 'chemistry': 2},
#     },
#     'user_2': {
#     }
# }
# print(person['user_1']['address'][1])

#homework from chatgpt
# me = {'name': 'Sergey',
#       'age': 28,
#       'city': 'Loznica'
# }
# print('Name:', me['name'])
# print('Age:', me['age'])
# print('City:', me['city'])

# me = {'name': 'Sergey',
#       'age': 28,
#       'city': 'Loznica',
#       'job': 'Python Developer'
#       }
# me['city'] = 'Belgrade'
# print(me)

# student = {
#     'name': 'Ivan',
#     'age': 20,
#     'grades': [4, 5, 3, 5, 4]
# }
# print('Grades:', student['grades'])
# print('Result:', sum(student['grades'])/len(student['grades']))
# i = sum(student['grades'])/len(student['grades'])
# student['status'] = i
# if i >= 4:
#     student['status'] = 'good'
# else:
#     student['status'] = 'bad'
# print('Status:', student['status'])
# print(student)