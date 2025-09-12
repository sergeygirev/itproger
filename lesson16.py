#modules (creating and importing)
# import time
# time.sleep(3)
# print("Hello World")

import datetime as d, sys, os, platform
# print(d.datetime.now())
# print(sys.path)
# print(os.name)
# print(platform.system())

# from math import sqrt as s, ceil
# print(ceil(s(100)))

# import mymodule as my
# print(my.name)
# my.hello()

# from mymodule import add_three_numbers as add
# print(add(5, 3, 6))

# import cowsay as c
# c.cow('Hello')

#homework rom chatgpt
# import math
# numb = int(input('Enter a number: '))
# print("Квадратный корень:", math.sqrt(numb))
# print("Факториал:", math.factorial(numb))
# print("Округление вверх:", math.ceil(numb))
# print("Округление вниз:", math.floor(numb))

# import math
# numb = int(input('Radius: '))
# print(2 * math.pi * numb)
# print(math.pi * (numb ** 2))

# import random
# numbers = [random.randint(1, 10) for i in range(5)]
# print("Список:", numbers)
# print("Случайный элемент:", random.choice(numbers))
# print(max(numbers))
# print(min(numbers))

# import datetime
# print(datetime.datetime.today())
# print(datetime.date.today())
# print(datetime.datetime.now().time())

# import datetime
# now = datetime.datetime.now()
# print("Дата и время:", now)
# print("Только дата:", now.date())
# print("Только время:", now.time())

# import datetime
# now = datetime.datetime.now()
# print('today:', now.date())
# print('after 1 week:', now.date() + datetime.timedelta(weeks=1))

# import datetime
# today = datetime.date.today()
# newyear = datetime.date(today.year + 1, 1, 1)
# print('today:', today)
# print('till new year:', (newyear - today).days)