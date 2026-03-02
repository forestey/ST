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
from asyncio import current_task
from sys import prefix
from tokenize import single_quoted

from numpy.f2py.crackfortran import previous_context
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

# class Queue:
#     def __init__(self):
#         self._items = []
#
#     def __str__(self):
#         return f"{self._items}"
#
#     def is_empty(self):
#         return not bool(self._items)
#
#     def enqueue(self, item):
#         self._items.insert(0, item)
#
#     def dequeue(self):
#         return self._items.pop()
#
#     def size(self):
#         return len(self._items)
#
# q = Queue()
# print(q.is_empty())
# q.enqueue(4)
# q.enqueue("Dog")
# q.enqueue("True")
# q.enqueue(8.4)
# print(q)
# print(q.size())
# print(q.is_empty())
# print(q.dequeue())
# print(q.size())
# print(q.dequeue())
# print(q.size())

# 传土豆模拟程序
# from pythonds3.basic import Queue
#
# def hot_potato(name_list, num):
#     sim_queue = Queue()
#     for name in name_list:
#         sim_queue.enqueue(name)
#     while sim_queue.size() > 1:
#         for i in range(num):
#             sim_queue.enqueue(sim_queue.dequeue())
#
#         sim_queue.dequeue()
#     return sim_queue.dequeue()
#
# print(hot_potato(name_list=['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'],num=7))

# 打印机队列：创建3个类Printer\Task\PrintQueue
# class Printer:
#     def __init__(self, ppm):
#         self.page_rate = ppm
#         self.current_task = None
#         self.time_remaining = 0
#
#     def tick(self):
#         if self.current_task is not None:
#             self.time_remaining = self.time_remaining - 1
#             if self.time_remaining <= 0:
#                 self.current_task = None
#
#     def busy(self):
#         return self.current_task is not None
#
#     def start_next(self, new_task):
#         self.current_task = new_task
#         self.time_remaining = new_task.get_pages()*60/self.page_rate
#
# import random
# class Task:
#     def __init__(self, time):
#         self.timestamp = time
#         self.pages = random.randrange(1, 21)
#
#     def get_stamp(self):
#         return self.timestamp
#
#     def get_pages(self):
#         return self.pages
#
#     def wait_time(self, current_time):
#         return current_time - self.timestamp
#
# from pythonds3.basic import Queue
#
# def simulation(num_seconds, pages_per_minute):
#     lab_printer = Printer(pages_per_minute)
#     print_queue = Queue()
#     waiting_times = []
#
#     for current_seconds in range(num_seconds):
#         if new_print_task():
#             task = Task(current_seconds)
#             print_queue.enqueue(task)
#
#         if (not lab_printer.busy()) and (not print_queue.is_empty()):
#             nexttask = print_queue.dequeue()
#             waiting_times.append(nexttask.wait_time(current_seconds))
#             lab_printer.start_next(nexttask)
#
#         lab_printer.tick()
#
#     average_wait = sum(waiting_times) / len(waiting_times)
#     print(f"Average wait: {average_wait:6.2f} secs + {print_queue.size():1d} tasks remaining.")
#
# def new_print_task():
#     num = random.randrange(1, 181)
#     return num == 180
#
# for i in range(10):
#     simulation(3600, 10)

# 用python实现双端队列
# class Deque:
#     def __init__(self):
#         self._items = []
#
#     def __str__(self):
#         return f"{self._items}"
#
#     def is_empty(self):
#         return not bool(self._items)
#
#     def add_front(self, item):
#         # 将元素添加到双端队列前端
#         self._items.append(item)
#
#     def add_rear(self, item):
#         # 将元素添加到双端队列后端
#         self._items.insert(0, item)
#
#     def remove_front(self):
#         return self._items.pop()
#
#     def remove_rear(self):
#         return self._items.pop(0)
#
#     def size(self):
#         return len(self._items)
#
# d = Deque()
# print(d.is_empty())
# d.add_rear(4)
# d.add_front('Cat')
# d.add_front('Dog')
# d.add_front('True')
# print(d)
# print(d.size())
# print(d.is_empty())
# d.add_rear(8.4)
# print(d)
# print(d.remove_rear())
# print(d.remove_front())
#
# # 回文检测器:radar\madam\toot等
# def pal_checker(a_string):
#     char_deque = Deque()
#     for ch in a_string:
#         char_deque.add_rear(ch)
#
#     while char_deque.size() > 1:
#         first = char_deque.remove_front()
#         last = char_deque.remove_rear()
#         if first != last:
#             return False
#     return True
#
# print(pal_checker("ldjfoprekw"))
# print(pal_checker("rafar"))

# 链表
# Node类:链表节点
class Node:
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        return self._data

    def set_data(self, node_data):
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        return self._next

    def set_next(self, node_next):
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        return f"{self._data}"

print(Node(93).data)

class UnorderedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
        if __name__ == '__main__':
            current = current.next
        return count

    def search(self, item):
        current = self._head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        current = self._head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next
            if current is None:
                raise ValueError(f"{item} is not in the list")
            if previous is None:
                self._head = current.next
            else:
                previous.next = current.next
