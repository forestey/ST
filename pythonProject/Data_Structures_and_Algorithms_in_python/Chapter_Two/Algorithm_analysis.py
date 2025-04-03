import time
def sumOfN(n):
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum += i

    end = time.time()
    return theSum, end-start

for i in range(5):
    print("Sim is %d required %10.7f seconds" % sumOfN(1000000))

# 使用公式来计算n个整数之和
def sumOfN_1(n):
    return (n*(n-1) / 2)

for i in range(5):
    print("Sim is %d required %10.7f seconds" % sumOfN_1(1000000))