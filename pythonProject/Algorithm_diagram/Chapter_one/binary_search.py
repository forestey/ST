import random

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        count += 1
        if guess == item:
            return mid, count
        if guess > item:
            print("Guess is lower")
            high = mid - 1
        else:
            print("Guess is higher")
            low = mid + 1

my_list = range(1, 256)
print(binary_search(my_list, random.randint(1,256)))

print(2**8)
