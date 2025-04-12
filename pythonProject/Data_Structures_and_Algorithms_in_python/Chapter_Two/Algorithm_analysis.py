import time
from timeit import Timer
import random
import timeit
# def sumOfN(n):
#     start = time.time()
#
#     theSum = 0
#     for i in range(1, n+1):
#         theSum += i
#
#     end = time.time()
#     return theSum, end-start
#
# for i in range(5):
#     print("Sim is %d required %10.7f seconds" % sumOfN(1000000))
#
# # 使用公式来计算n个整数之和
# def sumOfN_1(n):
#     return (n*(n-1) / 2)
#
# for i in range(5):
#     print("Sim is %d required %10.7f seconds" % sumOfN_1(1000000))

# def test_1():
#     l = []
#     for i in range(1000):
#         l = l + [i]
#
# def test_2():
#     l = []
#     for i in range(1000):
#         l.append(i)
#
# def test_3():
#     l = [i for i in range(1000)]
#
# def test_4():
#     l = list(range(10000))
#
# t1 = Timer("test_1()", "from __main__ import test_1")
# print(f"Concatenation: {t1.timeit(number=1000):15.5f} milliseconds")
#
# t2 = Timer("test_2()", "from __main__ import test_2")
# print(f"Appending: {t2.timeit(number=1000):15.5f} milliseconds")
#
# t3 = Timer("test_3()", "from __main__ import test_3")
# print(f"List comprehension: {t3.timeit(number=1000):15.5f} milliseconds")
#
# t4 = Timer("test_4()", "from __main__ import test_4")
# print(f"List range: {t4.timeit(number=1000):15.5f} milliseconds")


# x = [i for i in range(2000000)]
# x = list(range(2000000))
# pop_zero = Timer("x.pop(0)", "from __main__ import x")
# pop_end = Timer("x.pop()", "from __main__ import x")
# # print(x)
# print(f"pop(0): {pop_zero.timeit(number=1000):15.5f} milliseconds")
# print(f"pop(): {pop_end.timeit(number=1000):15.5f} milliseconds")


# pop_zero = Timer("x.pop(0)", "from __main__ import x")
# pop_end = Timer("x.pop()", "from __main__ import x")
# print(f"{'n':10s}{'pop(0)':>15s}{'pop()':>15s}")
# for i in range(1_000_000, 100_000_001, 1_000_000):
#     x = list(range(i))
#     pop_zero_t = pop_zero.timeit(number=1000)
#     x = list(range(i))
#     pop_end_t = pop_end.timeit(number=1000)
#     print(f"{i:<10d}{pop_zero_t:>15.5f}{pop_end_t:>15.5f}")

# 比较列表和字典的包含操作
# print(10_000, 1_000_001, 20_000)
print(f"{'n':10s}{'list':>10s}{'dict':>10s}")
for i in range(10_000, 1_000_001, 20_000):
    print(i)
    t_list = timeit.Timer(f"random.randrange({i}) in x_list", "from __main__ import random, x_list")
    t_dict = timeit.Timer(f"random.randrange({i}) in x_dict", "from __main__ import random, x_dict")
    x_list = list(range(i))

    list_time = t_list.timeit(number=1000)
    x_dict = {j: None for j in range(i)}
    # print(x_dict)
    dict_time = t_dict.timeit(number=1000)
    print(f"{i:<10}{list_time:>10.5f}{dict_time:>10.5f}")