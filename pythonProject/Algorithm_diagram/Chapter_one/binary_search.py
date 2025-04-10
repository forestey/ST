import random

# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#     count = 0
#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[mid]
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
# my_list = range(1, 256)
# print(binary_search(my_list, random.randint(1,256)))
#
# print(2**8)

# def quicksort(list_array):
#     if len(list_array) < 2:
#         return list_array
#     else:
#         pivot = list_array[0]
#         less = [i for i in list_array[1:] if i <= pivot]
#         greater = [i for i in list_array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)


# my_list = [random.randint(1, 1000) for i in range(1, 100)]
# print(my_list)
# print(quicksort(my_list))
# my_list = [5, 33, 5, 0, 78, 34, 12, 6, 9, 46]
# print(quicksort(my_list))

voted = {}

def check_voted(name):
    if voted.get(name):
        print("Kick them out")

    else:
        voted[name] = True
        print("Let them vote!")

check_voted("tom")
check_voted("mike")
check_voted("tom")
print(voted)