#constructors and method overriding
# class Cat:
#     name = None
#     age = None
#     isHappy = None
#
#     def __init__(self, name, age, isHappy):
#         self.set_data(name, age, isHappy)
#         self.get_data()
#
#     def set_data(self, name, age, isHappy = None):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_data(self):
#         print(self.name, 'age:',self.age, 'Happy:',self.isHappy)
#
# cat1 = Cat('John', 24, True)
# # cat1.get_data()
# cat1.set_data('Jon', 2)
# cat1.get_data()

#homework from chatgpt
# class Car:
#     def __init__(self, brand, year, mileage):
#         self.brand = brand
#         self.year = year
#         self.mileage = mileage
#
#     def set_data(self, brand, year, mileage):
#         self.brand = brand
#         self.year = year
#         self.mileage = mileage
#     def set_milage(self, mileage):
#         self.mileage = mileage
#     def get_info(self):
#         return 'brand: ' + self.brand + ', year: ' + str(self.year) + ', mileage: ' + str(self.mileage) + ' km'
# car1 = Car("Toyota", 2015, 12000)
# print(car1.get_info())
# car1.set_milage(1500)
# print(car1.get_info())

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    # def get_is_square(self):
    #     if self.width == self.height:
    #         return True
    #     else:
    #         return False

    # def get_is_square(self):
    #     return self.width == self.height
    # def get_area(self):
    #     return self.width * self.height
    # def get_perimeter(self):
    #     return 2 * self.width + 2 * self.height
# rect1 = Rectangle(5, 10)
# print(rect1.get_area())
# print(rect1.get_perimeter())
# rect1 = Rectangle(5, 10)
# print(rect1.get_is_square())
# rect2 = Rectangle(7, 7)
# print(rect2.get_is_square())