#basics of OOP (classes and objects)
# класс - чертеж робота
# объект - робот
# наследование - полезные опции робота
# полиморфизм - общий функционал, который можно переписать
# инкапсуляция - броня, защита
# поле == переменная (класс - поле, вне класса - переменная)

# class Cat:
#     name = None
#     age = None
#     isHappy = None
#
#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_data(self):
#         print(self.name, 'age:',self.age, 'Happy:',self.isHappy)
#
# cat1 = Cat()
# cat1.name = 'Barsik'
# cat1.age = 3
# cat1.isHappy = True
#
# cat2 = Cat()
# cat2.name = 'Bobik'
# cat2.age = 2
# cat2.isHappy = False
#
# cat3 = Cat()
# cat3.set_data('Fillip', 5, True)
#
# print(cat1.name)
# print(cat2.name)
# print(cat3.name)
#
# cat1.get_data()

#homework from chatgpt
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.grades = []
#     def add_grade(self, grade):
#         self.grades.append(grade)
#     def get_average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
# student1 = Student("Ivan", 20)
# student1.add_grade(5)
# student1.add_grade(4)
# student1.add_grade(3)
#
# print(student1.name)
# print(student1.get_average())

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def get_info(self):
#         return f'{self.title} - {self.author} ({self.year})'
#         return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"
#         return self.title + ' - ' + self.author + ' (' + str(self.year) + ')'
# book1 = Book('Harry Potter', 'Rowling', '1999')
# print(book1.get_info())