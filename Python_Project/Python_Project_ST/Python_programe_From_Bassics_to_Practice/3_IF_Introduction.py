cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    # if car == 'bmw':
    if car.lower()=='bmw':
        print(car.upper())
    else:
        print(car.title())

age = 19
if age >= 18:
    print("You are old enough to vote!")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost id $" + str(price)+".")


request_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for request_topping in request_toppings:
    if request_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + request_topping + ".")
print ("Finished making your pizza!")

request_toppings = []
if request_toppings:
    for request_topping in request_toppings:
        print("Adding " + request_topping + ".")
    print ("Finished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")