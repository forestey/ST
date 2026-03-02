from Car_class_7_0 import Car

my_car = Car('audi', 'a4', 2024)
print(my_car.get_descriptive_name())

my_car.odometer_reading = 500
my_car.read_odometer()