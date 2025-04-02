"""
1、定义类时首字母大写
2、类中的函数被称为方法，有关函数的一切都适用于方法，唯一重要的差别是调用方法的方式
3、__init__()是一个特殊的方法，每当根据类创建实例时，python都会自动运行它。在这个方法的名称中，开关和末尾各有两个下划线，这是一种约定，
旨在避免Python默认方法与普通方法发生名称冲突。
"""
# class Dog:
#     # 模拟小狗的属性
#     def __init__(self, name, age):
#         # 初始化属性name和age
#         self.name = name
#         self.age = age
#
#     # 模拟小狗蹲下
#     def sit(self):
#         print(self.name.title() + " is now sitting")
#
#     # 模拟小狗打滚
#     def roll_over(self):
#         print(self.name.title() + " rolled over!")
#
# my_dog = Dog("Eric",10)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog's age is " + str(my_dog.age) + " years old" + ".")
#
# my_dog.sit()
# my_dog.roll_over()
#
# other_dog = Dog("lucy",10)
# print("\nMy dog's name is " + other_dog.name.title() + ".")
# print("My dog's age is " + str(other_dog.age) + " years old" + ".")
#
# other_dog.sit()
# other_dog.roll_over()

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
# my_new_car = Car('audi', 'a4', '2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# 修改属性的值
# 1.直接修改属性的值
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
# my_new_car = Car('audi', 'a4', '2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 50
# my_new_car.read_odometer()

# 2.通过方法修改属性的值
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         self.odometer_reading = mileage
#
# my_new_car = Car('audi', 'a4', '2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(100)
# my_new_car.read_odometer()

#禁止任何人将里程数往回调
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 1000
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
# my_new_car = Car('audi', 'a4', '2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(100)
# my_new_car.read_odometer()

# 通过方法对属性的值进行递增;有时候需要将属性值递增特定的量，而不是将其设置为全新的值。
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 1000
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         if miles > 0:
#             self.odometer_reading += miles
#         else:
#             print("The mileage cannot be negative!")
#
# my_new_car = Car('audi', 'a4', '2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(35400)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(-10)
# my_new_car.read_odometer()

# 继承：如果要编写的类是另一个现成类的特殊版本，可使用继承。一个类继承另一个类时，将自动获得另一个类的所有属性和方法；原有的类称为父类，而新类称为子类。
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 1000
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         if miles > 0:
#             self.odometer_reading += miles
#         else:
#             print("The mileage cannot be negative!")
#
# """
# 定义一个子类电动汽车，它继承Car的所有属性
# """
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         # 初始化父类的属性
#         super().__init__(make, model, year)
#
# my_tesla = ElectricCar('tesla', 'model s', 2024)
# print(my_tesla.get_descriptive_name())
# my_tesla.update_odometer(35400)
# my_tesla.read_odometer()
# my_tesla.increment_odometer(-10)
# my_tesla.read_odometer()

# 给子类定义属性和方法
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 1000
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         if miles > 0:
#             self.odometer_reading += miles
#         else:
#             print("The mileage cannot be negative!")
#
# """
# 定义一个子类电动汽车，它继承Car的所有属性
# """
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         # 初始化父类的属性
#         super().__init__(make, model, year)
#         self.battery_size = 90
#
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
# my_tesla = ElectricCar('tesla', 'model s', 2024)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

# 重写父类的方法；在子类中如果继承的父类方法不符合子类的要求，子类可以对其方法进行重写。为此，可在子类中定义一个方法，它与父类的方法同名。
# 这样Python就不会考虑父类的同名方法，只会关注子类中的同名方法

# 将实例用作属性
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 1000
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         if miles > 0:
#             self.odometer_reading += miles
#         else:
#             print("The mileage cannot be negative!")
#
# class Battery:
# # 电动汽车电瓶的属性
#     def __init__(self, battery_size=70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-Kwh battery.")
#
#     def get_range(self):
#         if self.battery_size == 70:
#             distance = 300
#         elif self.battery_size == 85:
#             distance = 350
#         else:
#             print("Not support other distance")
#         message = "This car can go approximately " + str(distance)
#         message += " miles on a full battery."
#         print(message)
#
# """
# 定义一个子类电动汽车，它继承Car的所有属性
# """
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         # 初始化父类的属性
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
# my_tesla = ElectricCar('tesla', 'model s', 2024)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# 模拟实物

# 导入单个类
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("The mileage cannot be negative!")
