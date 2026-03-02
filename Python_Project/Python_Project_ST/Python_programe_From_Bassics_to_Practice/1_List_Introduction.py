# 3.1 姓名：将一些朋友的姓名存储在一个列表中，并将其命名为names.依次访问列表中的每个元素，从而将每个朋友的姓名都打印出来
names = ['Jack', 'Jay', 'Alex', 'Marlin', 'Jerry', 'Tom', 'Eric']
print("I have many friends, as following with:")
for i in names:
    # print(i)
    # 3.2 问候语：使用3.1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息包含相同的问候语，但抬头为相应朋友的姓名。
    print(i + ":Good morning！")

# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducat'
print(motorcycles)

# 列表中添加元素
# 末尾添加新元素append
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducat')
print(motorcycles)
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('jialing')
motorcycles.append('125')
print(motorcycles)
tmp = "qianjiang"
motorcycles.append(tmp)
print(motorcycles)

# 插入列表insert
motorcycles.insert(0, 'Yuqiling')
print(motorcycles)

# 列表中删除元素del
# del使用时需要知道该元素在列表中的索引
del motorcycles[0]
print(motorcycles)
del motorcycles[-2]
print(motorcycles)
# 有时候，需要将元素从列表中删除，并接着使用它的值。pop可删除列表末尾的元素，并让你能够接着使用它。
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")
# 如果要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续使用它，就使用方法pop()
print(motorcycles)
motorcycles.remove('jialing')
print(motorcycles)
# 3-4 嘉宾名单
Guest_list = ['Alex', 'Tom', 'Jerry', 'lisa', 'Jack']
print(f"I want to invite {Guest_list} to dinner")
Guest_list = ['Alex', 'Tom', 'Jerry', 'lisa', 'Jack']
print(f"{Guest_list[-1]} can't have dinner with me,I want to invite other friend to dinner")
del Guest_list[-1]
Guest_list.append('Kevin')
print(f"I want to invite {Guest_list} to dinner")
print(Guest_list)
del Guest_list[:]
print(Guest_list)
# sort按字母顺序排序，修改是永久性的
Guest_list = ['Alex', 'Tom', 'Jerry', 'lisa', 'Jack']
Guest_list.sort()
print(Guest_list)
# 按字母顺序相反的顺序排列列表，修改是永久性的
Guest_list.sort(reverse=True)
print(Guest_list)

# 使用sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
# 临时排序
print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars, reverse=True))
# 原始列表排序不变
print("\nHere is the original list again:")
print(cars)

# 反转列表用reverse()方法,永久性地修改列表元素的排列顺序，若要恢复只需再次使用reverse()即可。
Guest_list = ['Alex', 'Tom', 'Jerry', 'lisa', 'Jack']
print(Guest_list)
Guest_list.reverse()
print(Guest_list)

# 确定列表的长度len()
print(len(Guest_list))

Guest_list = ['Alex', 'Tom', 'Jerry', 'lisa', 'Jack']
for guest_list in Guest_list:
    print(guest_list)
    print(guest_list.title() + ", that was a great trick")

Pizzas = ['Domino\'s', 'Pizza Hut', 'Sbarro']
for pizza in Pizzas:
 print(f"Pizza brands is {pizza}")

for values in range(1,6):
    print(values)
numbers = list(range(1,11,2))
print(numbers)
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares = [value ** 2 for value in range(1,11)]
print(squares)

# 切片
players = ['charles', 'martina', 'michel', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:2])
print(players[1:])
print(players[-2:])
for player in players[:3]:
    print(player.title())

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('cannoli')
print(f"My favorite foods are: {my_foods}")
print(f"My friend's favorite foods are: {friend_foods}")