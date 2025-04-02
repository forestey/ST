# 打开文件
# with open(r'text_files\pi_digits.txt') as file_object:
#     contents = file_object.read()
#     # rstrip():删除字符串末尾的空白;strip()删除左边的空格
#     print(contents.rstrip())

# file_path = r'F:\ST\pythonProject\Python_programe_From_Bassics_to_Practice\File_exception_8\text_files\pi_digits.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
#     # rstrip():删除字符串末尾的空白
#     print(contents.rstrip())

# file_path = r'F:\ST\pythonProject\Python_programe_From_Bassics_to_Practice\File_exception_8\text_files'
# with open(file_path + r'\pi_digits.txt') as file_object:
#     contents = file_object.read()
#     # rstrip():删除字符串末尾的空白
#     print(contents.rstrip())

# 逐行读取
# filename = r'text_files\pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rsplit())

# filename = r'text_files\pi_digits.txt'
# with open(filename) as file_object:
#     # readline()读取文件的一行，readlines()读取文件的每一行
#     lines = file_object.readlines()
#
# for line in lines:
#     print(line.rsplit())

# 使用文件的内容
# filename = r'text_files\pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
# print(type(lines))
# pi_string = ''
# for line in lines:
#     pi_string += line
#
# print(type(pi_string))
# print(pi_string)
# print(len(pi_string))

# filename = r'text_files\pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
# print(type(lines))
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(type(pi_string))
# print(pi_string)
# print(len(pi_string))
# 处理百万行级的文件
# file_name = r'text_files\pi_million_digits.txt'
#
# with open(file_name) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string[:502] + "...")
# print(len(pi_string))

# 查看自己的生日是否包含在Pi中
# file_name = r'text_files\pi_million_digits.txt'
#
# with open(file_name) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# birthday = input("Enter you birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi")
# else:
#     print("Your birthday does not appear in the first million digits of pi")

# 写入文件;如果要写入的内容文件存在，python将在返回文件对象前清空该文件
file_name = r'text_files\programming.txt'

# with open(file_name, 'w') as file_object:
#     file_object.write("I love programming.")
#
# with open(file_name, 'w') as file_object:
#     file_object.write("I love creating new games.")

# 写入多行内容
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 附加到文件：要给文件添加内容，而不是覆盖原有的内容，可以附加模式打开文件。如果写入的文件不存在将会自动创建一个空文件来写入
with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")