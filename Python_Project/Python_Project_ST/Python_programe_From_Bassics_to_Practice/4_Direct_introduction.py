from ctypes import c_int8

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0['color'])

alien_0 = {'x_position': 0,'y_position': 25,'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 删除键值对
alien_0 = {'color': 'green', 'points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print(favorite_languages)
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# 遍历所有的键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

for key, value in favorite_languages.items():
    print(key.title() + "'s favorite language is " + value.title() + ".")

# 遍历字典时，会默认遍历所有的键，所以以下两种方式都是遍历字典的键。加上keys可以让代码更加容易理解
for name in favorite_languages.keys():
    print(name.title())
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + "' thank you for taking the poll.")

# 遍历字典的值
for name in favorite_languages.values():
    print(name.title())
# 剔除重复的项，使用set
for language in set(favorite_languages.values()):
    print(language.title())

# 嵌套：将字典存储在列表中，或将列表存储在字典中
# 字典列表
# aline_0 = {'color': 'green', 'points': 5}
# aline_1 = {'color': 'yellow', 'points': 10}
# aline_2 = {'color': 'red', 'points': 15}
#
# aliens = [aline_0, aline_1, aline_2]
# for aline in aliens:
#     print(aline)

# aliens = []
# for aline_number in range(30):
#     new_aline = {'color': 'green', 'points':5, 'speed': 'slow'}
#     aliens.append(new_aline)
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print("Total number of aliens: " + str(len(aliens)))

aliens = []
for aline_number in range(30):
    new_aline = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_aline)
    print(aliens)
print(f"all aliens elements : {aliens}")
for alien in aliens[:3]:
    print(alien)
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    print(alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

# 列表字典
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crush pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print(topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(name.title() + "'s favorite languages is " + languages[0].title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())

# 字典存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username.title())
    full_name = user_info['first'] + " " + user_info['last']
    print("Full name: " + full_name.title())
    location = user_info['location']
    print("Location: " + location.title())
