# 栈的实现
# class Stack:
#     # "将栈实现为列表"
#     def __init__(self):
#         self._items = [] # 创建新栈
#
#     def __str__(self):
#         return f"{self._items}"
#
#     def is_empty(self):
#         # 检查栈是否为空
#         return not bool(self._items)
#
#     def push(self, item):
#         # 向栈添加元素
#         self._items.append(item)
#
#     def pop(self):
#         # 移除栈顶元素
#         return self._items.pop()
#
#     def peek(self):
#         # 获取栈顶元素的值
#         return self._items[-1]
#
#     def size(self):
#         # 获取栈中元素数量
#         return len(self._items)
#
#
#
# # from pythonds3.basic import Stack
# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push(3.8)
# s.push('Dog')
# s.push('True')
# print(s)
# print(s.pop())
# print(s.peek())
# print(s.size())

# 栈的另一种实现
# class Stack:
#     # "将栈实现为列表"
#     def __init__(self):
#         self.items = [] # 创建新栈
#
#     def __str__(self):
#         return f"{self.items}"
#
#     def is_empty(self):
#         # 检查栈是否为空
#         return self.items == []
#
#     def push(self, item):
#         # 向栈添加元素
#         self.items.insert(0, item)
#
#     def pop(self):
#         # 移除栈顶元素
#         return self.items.pop(0)
#
#     def peek(self):
#         # 获取栈顶元素的值
#         return self.items[0]
#
#     def size(self):
#         # 获取栈中元素数量
#         return len(self.items)
#
#
#
# # from pythonds3.basic import Stack
# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push(3.8)
# s.push('Dog')
# s.push('True')
# print(s)
# print(s.pop())
# print(s.peek())
# print(s.size())

# 十进制转换为二进制算法
# from pythonds3.basic import Stack
# def divide_by_2(decimal_num):
#     rem_stack = Stack()
#
#     while decimal_num > 0:
#         # print(f"decimal_num={decimal_num}")
#         rem = decimal_num % 2
#         rem_stack.push(rem)
#         print(rem_stack.peek())
#         decimal_num = decimal_num // 2
#         print(f"decimal_num={decimal_num}")
#
#     bin_string = ""
#     while not rem_stack.is_empty():
#         bin_string = bin_string + str(rem_stack.pop())
#         print(f"bin_string={bin_string}")
#
#     return bin_string
#
# print(divide_by_2(233))
#


# 将十进制转换成任意进制数算法
# from pythonds3.basic import Stack
# def base_converter(decimal_num, base):
#     digits = "0123456789ABCDEF"
#     rem_stack = Stack()
#
#     while decimal_num > 0:
#         rem = decimal_num % base
#         rem_stack.push(rem)
#         print(f"rem_stack_peek={rem_stack.peek()}")
#         decimal_num = decimal_num // base
#         print(f"decimal_num={decimal_num}")
#
#     new_string = ""
#     while not rem_stack.is_empty():
#         new_string += digits[rem_stack.pop()]
#         print(f"bin_string={new_string}")
#
#     return new_string
#
# print(base_converter(13,16))

# 中序到前序表达式的转换
from pythonds3.basic import Stack
# def infix_to_postfix(infix_expr):
#     prec = {}
#     prec["*"] = 3
#     prec["/"] = 3
#     prec["+"] = 2
#     prec["-"] = 2
#     prec["("] = 1
#     op_stack = Stack()
#     postfix_list = []
#     token_list = infix_expr.split()
#
#     for token in token_list:
#         if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
#             postfix_list.append(token)
#         elif token == "(":
#             op_stack.push(token)
#         elif token == ")":
#             top_token = op_stack.pop()
#             while top_token != "(":
#                 postfix_list.append(top_token)
#                 top_token = op_stack.pop()
#         else:
#             while not (op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
#                 postfix_list.append(op_stack.pop())
#             op_stack.push(token)
#
#     while not op_stack.is_empty():
#         postfix_list.append(op_stack.pop())
#     return " ".join(postfix_list)
#
# print(infix_to_postfix("(A+B)*C"))

# 中序到后序表达式的转换

# from pythonds3.basic import Stack
# def postfix_eval(postfix_expr):
#     operand_stack = Stack()
#     token_list = postfix_expr.split()
#
#     for token in token_list:
#         if token in "0123456789":
#             operand_stack.push(int(token))
#         else:
#             operand_2 = operand_stack.pop()
#             operand_1 = operand_stack.pop()
#             result = do_math(token, operand_1, operand_2)
#             operand_stack.push(result)
#     return operand_stack.pop()
#
# def do_math(op, op_1, op_2):
#     if op == "+":
#         return op_1 * op_2
#     elif op == "/":
#         return op_1 / op_2
#     elif op == "+":
#         return op_1 + op_2
#     else:
#         return op_1 - op_2
#
# print(postfix_eval("(A+B)*(C+D)"))

# 用python实现队列

class Queue:
    def __init__(self):
        self._items = []

    def __str__(self):
        return f"{self._items}"

    def is_empty(self):
        return not bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

q = Queue()
print(q.is_empty())
q.enqueue(4)
q.enqueue("Dog")
q.enqueue("True")
q.enqueue(8.4)
print(q)
print(q.size())
print(q.is_empty())
print(q.dequeue())
print(q.size())
print(q.dequeue())
print(q.size())