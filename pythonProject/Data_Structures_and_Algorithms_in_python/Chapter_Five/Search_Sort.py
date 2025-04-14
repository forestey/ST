# 搜索算法
# def sequential_search(a_list, item):
#     pos = 0
#     while pos < len(a_list):
#         if a_list[pos] == item:
#             return True
#         pos += 1
#     return False
#
# print(sequential_search(a_list=[1,2,3,4,55,33,88,55,86,91], item=9))

# 有序排列的搜索算法
# def ordered_sequential_search(a_list, item):
#     pos = 0
#     while pos < len(a_list):
#         if a_list[pos] == item:
#             return True
#         if a_list[pos] > item:
#             return False
#         pos += 1
#
#     return False
#
# print(ordered_sequential_search(a_list=[1,2,3,4,55,33,88,55,86,91], item=9))

# 二分搜索
# import random
# def binary_search(a_list, item):
#     low = 0
#     high = len(a_list) - 1
#     count = 0
#     while low <= high:
#         mid = (low + high) // 2
#         guess = a_list[mid]
#         count += 1
#         if guess == item:
#             return mid, count
#         if guess > item:
#             print("Guess is lower")
#             high = mid - 1
#         else:
#             print("Guess is higher")
#             low = mid + 1
#
# print(binary_search(a_list=range(1, 256), item=random.randint(1,256)))

# def binary_search(a_list, item):
#     first = 0
#     last = len(a_list) - 1
#
#     while first <= last:
#         midpoint = (first + last) // 2
#         if item == a_list[midpoint]:
#             return midpoint, True
#         elif item > a_list[midpoint]:
#             first = midpoint + 1
#         else:
#             last = midpoint - 1
#
#     return False
#
# print(binary_search(a_list=range(1, 256), item=random.randint(1,256)))
# # 二分搜索的递归版本
# def binary_search_rec(a_list, item):
#     if len(a_list) == 0:
#         return False
#     midpoint = len(a_list) // 2
#     if item == a_list[midpoint]:
#         return True
#     elif item < a_list[midpoint]:
#         return binary_search_rec(a_list=a_list[:midpoint], item=item)
#     else:
#         return binary_search_rec(a_list=a_list[(midpoint+1):], item=item)
#
# print(binary_search_rec(a_list=range(1, 256), item=random.randint(1,256)))

# 散列
