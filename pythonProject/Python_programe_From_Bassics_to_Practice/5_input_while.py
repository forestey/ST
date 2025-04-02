# input输入
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
# name = input("please enter your name: ")
# print("Hello, " + name + "!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print("Hello, " + name + "!")

# int()它让Python将输入视为数值，可以将字符串转换为数值表示
# age = input("How old are you? ")
# age = int(age)
# print(age >= 18)

# 求模运算%，它将两个数相除并返回余数
# print(4%3)

# While
# for循环用于针对集合中的每个元素的一个代码块，而while循环不断运行，直到指定的条件不满足为止
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "Tell me something, and I will repeat it back to you: "
# prompt += "Enter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = "Tell me something, and I will repeat it back to you: "
# prompt += "Enter 'quit' to end the program."
# active_flag = True
# while active_flag:
#     message = input(prompt)
#     if message == 'quit':
#         active_flag = False
#     else:
#         print(message)

# break停止循环
# prompt = "Tell me something, and I will repeat it back to you: "
# prompt += "Enter 'quit' to end the program."
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

# continue返回到循环开头
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#
#     print(current_number)

# while处理列表和循环
# 创建一个待验证用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#
# # 验证每个用户，直到没有未验证用户为止；将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print(confirmed_users)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除包含特定值的所有列表元素
pets = ['dog', 'dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)