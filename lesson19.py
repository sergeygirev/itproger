#inheritance, encapsulation, polymorphism
# class Building:
#     __year = None
#     __city = None
#
#     def __init__(self, year, city):
#         self.year = year
#         self.city = city
#
#     def get_info(self):
#         print('Year:', self.year, '. City:', self.city)
#
# class School(Building):
#     pupils = 0
#
#     def __init__(self, pupils, year, city):
#         super(School, self).__init__(year, city)
#         self.pupils = pupils
#     def get_info(self):
#         super().get_info()
#         print('Pupils:', self.pupils)
# class House(Building):
#     pass
# class Shop(Building):
#     pass
# school = School(100,2000, 'Moscow')
# school.year = 2001
# school.get_info()
# school = Building(2000, 'Moscow')
# house = House(2000, 'Moscow')
# shop = Shop(2000, 'Moscow')

#homework from chatgpt
# class Animal:
#     def speak(self):
#         print('Animal is speaking')
# class Dog(Animal):
#     def speak(self):
#         print('Woof')
# dog = Dog()
# dog.speak()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def get_info(self):
#         print('Name:', self.name, '. Salary:', self.salary)
# class Manager(Employee):
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)
#         self.bonus = bonus
#     def get_info(self):
#         print('Name:', self.name, '. Salary:', self.salary, ', bonus:', self.bonus)
# class Programmer(Employee):
#     def __init__(self, name, salary, language):
#         super().__init__(name, salary)
#         self.language = language
#     def get_info(self):
#         print('Name:', self.name, '. Salary:', self.salary, ', language:', self.language)
# manager = Manager('Ivan',2000, 500 )
# manager.get_info()
# programmer = Programmer('Stepan', 2000, 'Python')
# programmer.get_info()