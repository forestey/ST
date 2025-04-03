# print(7/3)
# print(3/6)
# print(3//2)
# print(3%2)
#
# print((55).__add__(21))
#
# print(list(range(10, 1, -1)))

# phone_ext = {'david':1410, 'brad':1137}
# print(phone_ext)
# print(phone_ext.keys())
# print(list(phone_ext.keys()))
# print(phone_ext.values())
# print(list(phone_ext.values()))

# 返回字典中所有键值对的dict_items对象
# print(phone_ext.items())
# print(list(phone_ext.items()))

# 返回k对应的值，如果没有则返回None
# print(phone_ext.get('kent'))
# 返回k对应的值，如果没有则返回No Entry
# print(phone_ext.get('kent', "No Entry"))

# aName = input("Please enter your name:")
# print("Your name in all capitals is", aName.upper(), "and has length", len(aName))

# print("Hello", "world")
# print('Hello', 'World', sep='***')
# print('Hello', 'World', end='***')

# 格式化字符串
# age = 23
# print("%s is %d years old." % (aName, age))
# price = 24
# item = 'banana'
# print("The %s costs %d cents" % (item, price))
# print("The %+10s costs %5.2f cents" % (item, price))
# print("The %+10s costs %10.2f cents" % (item, price))
#
# # 列表解析式
# sqlist = []
# for x in range(1,11):
#     sqlist.append(x*x)
# print(sqlist)
# # 可以一行代码来完成
# sqlist = [x*x for x in range(1,20)]
# print(sqlist)
#
# sqlist = [x*x for x in range(1,20) if x%2 !=0]
# print(sqlist)
#
# # 牛顿迭代法
# def square_root(n):
#     root = n/2
#     for k in range(20):
#         root = (1/2)*(root+(n/root))
#
#     return root
#
# print(square_root(9))
# 第一章：编程练习
# 1.实现简单的方法getNum和getDen ，它们分别返回分数的分子和分母。
# class Fraction:
#     def __init__(self, top, bottom):
#         self.num = top
#         self.den = bottom
#
#     def getNum(self):
#         return self.num
#
#     def getDen(self):
#         return self.den

# fractions = Fraction(3,5)
# print(fractions.getNum())
# print(fractions.getDen())

# 2.如果所有分数从一开始就是最简形式会更好。修改Fraction类的构造方法，立即使用最大公因数来化简分数。注意，这意味着__add__不再需要化简结果
# class Fraction:
#     def __init__(self, top, bottom):
#         self.num = top
#         self.den = bottom
#
#         for i in range(2, max(self.num, self.den)+1):
#             while self.num%i == 0 and self.den%i == 0:
#                 self.num //= i
#                 self.den //= i
#                 print(self.num, self.den)
#
# fractions = Fraction(8, 16)
# print(fractions)

# 3.实现下列简单的算术运算：sub 、mul 和__truediv__ 。
# 魔法方法
# class SubTest(object):
#     def __init__(self, age):
#         self.age = age
#
#     def __sub__(self, other):
#         print('call sub magic function')
#         return SubTest(self.age - other.age)
# num_1 = SubTest(18)
# num_2 = SubTest(10)
# print(f'sub result is:{(num_1 - num_2).age}')

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        print('newnum=', newnum)
        print('newden=', newden)
        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

# 4.实现下列关系运算：gt 、ge 、lt 、le 和__ne__ 。
    def __gt__(self, other):
        return self.num * other.den - self.den * other.num > 0

    def __ge__(self, other):
        return self.num * other.den - self.den * other.num >= 0

    def __lt__(self, other):
        return self.num * other.den - self.den * other.num < 0

    def __le__(self, other):
        return self.num * other.den - self.den * other.num <= 0

    def __ne__(self, other):
        return self.num * other.den - self.den * other.num != 0

# 5.修改Fraction 类的构造方法，使其检查并确保分子和分母均为整数。如果任一不是整数，就抛出异常。
class Fractions:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

        if isinstance(self.num, int) == False or isinstance(self.den, int) == False:
            raise RuntimeError("Error:TypeError,u should put int type")


# 6.我们假设负的分数是由负的分子和正的分母构成的。使用负的分母会导致某些关系运算符返回错误的结果。
# 一般来说，这是多余的限制。请修改构造方法，使得用户能够传入负的分母，并且所有的运算符都能返回正确的结果。
class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

        if self.den < 0:
            self.den = abs(self.den)
            self.num = self.num * -1

# 7.研究__radd__方法。它与__add__方法有何区别？何时应该使用它？请动手实现__radd__ 。
# _add_方法是算术运算符的重载，接收两个参数，返回它们的和，两个参数的值均不会改变。add(self, other)self + other加法
# _radd_方法是反向运算符的重载，接收两个参数，返回它们的和，两个参数的值均不会改变。radd(self, other)other + self加法
# 当运算符的左侧为内建类型时, 右侧为自定义类型进行算术匀算符运算时会出现TypeError错误, 因为无法修改内建类型的代码, 此时需要使用反向运算符的重载。

def __radd__(self, other):
    newnum = self.num * other.den + self.den * other.num
    newden = self.den * other.den
    return Fraction(newnum, newden)

# 8.研究__iadd__方法。它与__add__方法有何区别？何时应该使用它？请动手实现__iadd__ 。
# _iadd_方法是复合赋值算术运算符的重载，接收两个参数，改变第一个参数的值，所以对于不可变对象没有__iadd__方法。
# iadd(self, other） self += other加法
# 复合赋值算术运算符以x += y为例, 此运算符会优先调用x.iadd(y)方法, 如果没有__iadd__方法时,
# 则会将复合赋值算术运算拆解为: x = x + y, 然后调用x = x.add(y)方法, 如果再不存在__add__方法，则会触发TypeError类型的错误异常。
def __iadd__(self, other):
    # self += other
    newnum = self.num * other.den + self.den * other.num
    newden = self.den * other.den
    self.num = newnum
    self.den = newden
    return Fraction(self.num, self.den)

# 9.研究__repr__方法。它与__str__方法有何区别？何时应该使用它？请动手实现__repr__ 。
# _repr_与_str_的区别, 前者方便我们调试和记录日志, 后者给终端用户看。
# 当我们想所有环境下都统一显示的话，可以重构repr方法；当我们想在不同环境下支持不同的显示，例如终端用户显示使用str，而程序员在开发期间则使用底层的repr来显示，实际上str只是覆盖了repr以得到更友好的用户显示。

def __str__(self):
    return str(self.num) + "/" + str(self.den)


def __repr__(self):
    return '<%s / %s>' % (self.num, self.den)
    # return str(self.num) + "/" + str(self.den)


# 10.研究其他类型的逻辑门（例如与非门、或非门、异或门）。将它们加入电路的继承层次结构。你需要额外添加多少代码？

class NandGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1


class NorGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 1
        else:
            return 0


class XorGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 0
        else:
            return 1

# 11.最简单的算术电路是半加器。研究简单的半加器电路并实现它。半加器电路是指对两个输入数据位相加，输出一个结果位和进位，
# 没有进位输入的加法器电路。是实现两个一位二进制数的加法运算电路。
class HalfAdder():
    def __init__(self, n, A, B):
        self.label = n
        self.add1 = A
        self.add2 = B
        if self.add1 == self.add2:
            self.sum = 0
        else:
            self.sum = 1
        if self.add1 == 1 and self.add2 == 1:
            self.count = 1
        else:
            self.count = 0

    def __str__(self):
        return "%s-A: %s; B: %s; Sum: %s; Count: %s" % (self.label, self.add1, self.add2, self.sum, self.count)

# 12.将半加器电路扩展为8位的全加器。

class HalfAdder_8():
    def __init__(self, n, A, B):
        self.label = n
        self.add1 = A
        self.add2 = B
        if self.add1 + self.add2 == 8:
            self.sum = 0
        elif self.add1 + self.add2 < 8:
            self.sum = self.add1 + self.add2
        else:
            self.sum = (self.add1 + self.add2) % 8
        if self.add1 + self.add2 >= 8:
            self.count = 1
        else:
            self.count = 0

    def __str__(self):
        return "%s-A: %s; B: %s; Sum: %s; Count: %s" % (self.label, self.add1, self.add2, self.sum, self.count)

# 13.本章展示的电路模拟是反向工作的。换句话说，给定一个电路，其输出结果是通过反向访问输入值来产生的，这会导致其他的输出值被反向查询。这个过程一直持续到外部输入值被找到，此时用户会被要求输入数值。修改当前的实现，使电路正向计算结果。当收到输入值的时候，电路就会生成输出结果。
# 将get函数去掉，调用时直接赋值。【存疑】

# 14.设计一个表示一张扑克牌的类，以及一个表示一副扑克牌的类。使用这两个类实现你最喜欢的扑克牌游戏。
import random


class Card:
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['梅花', '方片', '红桃', '黑桃']

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = 'XX'
        return rep

    def pic_order(self):
        if self.rank == 'A':
            FaceNum = 1
        elif self.rank == 'J':
            FaceNum = 11
        elif self.rank == 'Q':
            FaceNum = 12
        elif self.rank == 'K':
            FaceNum = 13
        else:
            FaceNum = int(self.rank)
        if self.suit == '梅花':
            Suit = 1
        elif self.suit == '方片':
            Suit = 2
        elif self.suit == '红桃':
            Suit = 3
        else:
            Suit = 4
        return (Suit - 1) * 13 + FaceNum

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = '无牌'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Poke(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=13):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                else:
                    print('不能继续发牌咯，全发完啦~')


if __name__ == '__main__':
    print('性感荷官在线发牌~')
    players = [Hand(), Hand(), Hand(), Hand()]
    poke = Poke()
    poke.populate()
    poke.shuffle()
    poke.deal(players, 13)
    n = 1
    for hand in players:
        print('牌手', n, end=' :')
        print(hand)
        n = n + 1


# 15.在报纸上找到一个数独游戏，并编写一个程序求解。
# 此代码用的numpy我不太了解，后面学了再过来看，btw它没有用类，https: // blog.csdn.net / jingzhiyang / article / details / 126491903
# 临时找了一个还没看，插个眼回头补

import numpy as np


def generate_sudoku(mask_rate=0.5):
    while True:
        n = 9
        m = np.zeros((n, n), np.int)
        rg = np.arange(1, n + 1)
        m[0, :] = np.random.choice(rg, n, replace=False)
        try:
            for r in range(1, n):
                for c in range(n):
                    col_rest = np.setdiff1d(rg, m[:r, c])
                    row_rest = np.setdiff1d(rg, m[r, :c])
                    avb1 = np.intersect1d(col_rest, row_rest)
                    sub_r, sub_c = r // 3, c // 3
                    avb2 = np.setdiff1d(np.arange(0, n + 1),
                                        m[sub_r * 3:(sub_r + 1) * 3, sub_c * 3:(sub_c + 1) * 3].ravel())
                    avb = np.intersect1d(avb1, avb2)
                    m[r, c] = np.random.choice(avb, size=1)
            break
        except ValueError:
            pass
    print("Answer:\n", m)
    mm = m.copy()
    mm[np.random.choice([True, False], size=m.shape, p=[mask_rate, 1 - mask_rate])] = 0
    print("\nMasked anwser:\n", mm)
    np.savetxt("./puzzle.csv", mm, "%d", delimiter=",")
    return mm


def solve(m):
    if isinstance(m, list):
        m = np.array(m)
    elif isinstance(m, str):
        m = np.loadtxt(m, dtype=np.int, delimiter=",")
    rg = np.arange(m.shape[0] + 1)
    while True:
        mt = m.copy()
        while True:
            d = []
            d_len = []
            for i in range(m.shape[0]):
                for j in range(m.shape[1]):
                    if mt[i, j] == 0:
                        possibles = np.setdiff1d(rg, np.union1d(np.union1d(mt[i, :], mt[:, j]),
                                                                mt[3 * (i // 3):3 * (i // 3 + 1),
                                                                3 * (j // 3):3 * (j // 3 + 1)]))
                        d.append([i, j, possibles])
                        d_len.append(len(possibles))
            if len(d) == 0:
                break
            idx = np.argmin(d_len)
            i, j, p = d[idx]
            if len(p) > 0:
                num = np.random.choice(p)
            else:
                break
            mt[i, j] = num
            if len(d) == 0:
                break
        if np.all(mt != 0):
            break

    print("\nTrail:\n", mt)
    return mt


def check_solution(m):
    if isinstance(m, list):
        m = np.array(m)
    elif isinstance(m, str):
        m = np.loadtxt(m, dtype=np.int, delimiter=",")
    set_rg = set(np.arange(1, m.shape[0] + 1))
    no_good = False
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            r1 = set(m[3 * (i // 3):3 * (i // 3 + 1), 3 * (j // 3):3 * (j // 3 + 1)].ravel()) == set_rg
            r2 = set(m[i, :]) == set_rg
            r3 = set(m[:, j]) == set_rg
            if not (r1 and r2 and r3):
                no_good = True
                break
        if no_good:
            break
    if no_good:
        print("\nChecked: not good")
    else:
        print("\nChecked: OK")


if __name__ == "__main__":
    puzzle = generate_sudoku(mask_rate=0.7)
    solved = solve(puzzle)
    check_solution(solved)

    print("\nSolve in code:")
    solve([
        [0, 5, 0, 0, 6, 7, 9, 0, 0],
        [0, 2, 0, 0, 0, 8, 4, 0, 0],
        [0, 3, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 1, 0, 4],
        [0, 0, 0, 6, 0, 9, 0, 0, 0],
        [0, 0, 8, 5, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 9, 0, 0, 5, 0],
        [2, 1, 3, 7, 0, 0, 0, 0, 0]
    ])

    print("\nSolve in csv file:")
    solve("puzzle.csv")
