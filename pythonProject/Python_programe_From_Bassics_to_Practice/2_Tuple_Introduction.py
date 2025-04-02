# 元组使用圆括号来标识，列表使用方括号来标识；元组不能直接修改
dimensions = (200, 50)
print(dimensions)
# print(dimensions[0])
# print(dimensions[1])
for dimension in dimensions:
    print(dimension)
# 虽然不能修改元组的元素，但可以通过给存储元组的变量赋值，来重新定义整个元组
dimensions = (200, 50)
print(f"Original dimensions:{dimensions}")
dimensions = (632, 200)
print(f"Modified dimensions:{dimensions}")