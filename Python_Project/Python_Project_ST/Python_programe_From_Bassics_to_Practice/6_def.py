# return函数返回值
# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# 让实参变为可选的
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' +  last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hooker')
# print(musician)
# musician = get_formatted_name('jimi', 'hooker', 'lee')
# print(musician)

# 返回字典
# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)
#
# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', 41)
# print(musician)

# 向函数传递列表
# def greet_users(names):
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
#
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# 在函数中修改列表
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
#
# print(completed_models)
# print("The following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     print("The following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# print(unprinted_designs)
# show_completed_models(completed_models)

# 禁止函数修改列表可以用切片表示法
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     print("The following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs[:], completed_models)
# print(unprinted_designs)
# show_completed_models(completed_models)

# 传递任意数量的实参，*toppings：创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中。
# def make_pizza(*toppings):
#     print(toppings)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 结合使用位置实参和任意数量实参：如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。python先匹配位置和关键字实参，
# 再将余下的实参都收集到最后一个形参中。
# def make_pizza(size, *toppings):
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参，**user_info：创建一个名为user_info的空字典，并将收到的所有名称-值对都封装到这个字典中。
def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    # 使用字典的items返回该字典的所有键值对组成的元素
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)

# 导入整个模块 import module_name;调用模块中函数句点表示法module_name.function_name()
# 导入特定的函数 from module_name import function_name_0, function_name_2, function_name_3, ...调用模块里的函数function_name_0
# 给函数指定别名 from module_name import function_name as other_function_name主要用于调用的模块函数与主程序或其它调用的模块中的名称有冲突时使用
# 给模块指定别名 from module_name as other_module_name给模块指定别名
# 导入模块中的所有函数 from module_name import *可以通名称来调用每个函数function_name()，而无需使用句点表示法module_name.function_name()
# 在导入模块时最佳的做法是：要么只导入你需要使用的函数，要么使用import导入整个模块并使用句点表示法。