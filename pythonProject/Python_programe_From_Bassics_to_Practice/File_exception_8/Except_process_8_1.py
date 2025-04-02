# try-except来处理异常
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# from Python_programe_From_Bassics_to_Practice.File_exception_8.File_process_8_0 import file_name
import json


# 使用异常避免崩溃；发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤为重要。

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)
# file_name = 'alice.txt'
#
# try:
#     with open(file_name) as file_object:
#         contents = file_object.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + file_name + " does not exist."
#     print(msg)

# 分析文本
# title = "Alice in Wonderland!"
# print(title.split())

# file_name = r'text_files\alice.txt'

# try:
#     with open(file_name) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + file_name + " does not exist."
#     print(msg)
# else:
#     words = contents.split()
#     print(words)
#     num_words = len(words)
#     print("The file " + file_name + " has about " + str(num_words) + " words.")

# def count_words(filename):
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         msg = "Sorry, the file " + filename + " does not exist."
#         print(msg)
#     else:
#         words = contents.split()
#         # print(words)
#         num_words = len(words)
#         print("The file " + filename + " has about " + str(num_words) + " words.")
#
# file_names = [r'text_files\alice.txt', r'text_files\siddhartha.txt', r'text_files\little_women.txt']
# for file_name in file_names:
#     count_words(file_name)

# 出现异常一声不吭
# def count_words(filename):
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         pass
#     else:
#         words = contents.split()
#         # print(words)
#         num_words = len(words)
#         print("The file " + filename + " has about " + str(num_words) + " words.")
#
# file_names = [r'text_files\alice.txt', r'text_files\siddhartha.txt', r'text_files\little_women.txt']
# for file_name in file_names:
#     count_words(file_name)

# 存储数据
# import json
# numbers = [2, 3, 5, 7, 11, 13, 15]
# filename = r'text_files\numbers.json'
# with open(filename, 'w') as f_obj:
#     # noinspection PyTypeChecker
#     json.dump(numbers, f_obj)
#
# with open(filename) as f_obj_read:
#     number = json.load(f_obj_read)
# print(number)

# 保存和读取用户生成的数据
# import json
# username = input("Enter your username: ")
#
# filename = r'text_files\username.json'
# with open(filename, 'w') as f_obj:
#     # noinspection PyTypeChecker
#     json.dump(username, f_obj)
#     print("We'll remember you when you come back, " + username + "!")
#
# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print("Welcome back, " + username + "!")

# import json
# def greet_user():
#     filename = r'text_files\username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("Enter your username: ")
#         with open(filename, 'w') as f_obj:
#             # noinspection PyTypeChecker
#             json.dump(username, f_obj)
#             print("We'll remember you when you come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")
#
# greet_user()


 # 重构
# import json
# filename = r'text_files\username.json'
# def get_stored_username():
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
# def greet_user():
#     username = get_stored_username()
#     if username:
#         print("Welcome back, " + username + "!")
#     else:
#         username = input("Enter your username: ")
#         with open(filename, 'w') as f_obj:
#             # noinspection PyTypeChecker
#             json.dump(username, f_obj)
#             print("We'll remember you when you come back, " + username + "!")
#
# greet_user()

import json
filename = r'text_files\username.json'
def get_stored_username():
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("Enter your username: ")
    with open(filename, 'w') as f_obj:
        # noinspection PyTypeChecker
        json.dump(username, f_obj)
        return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()