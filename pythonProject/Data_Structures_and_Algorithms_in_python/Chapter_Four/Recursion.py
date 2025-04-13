# def list_sum(num_list):
#     the_sum = 0
#     for i in num_list:
#         the_sum += i
#     return the_sum
# print(list_sum([1,3,5,7,9,11,13]))

# def list_sum(num_list):
#     if len(num_list) == 1:
#         return num_list[0]
#     else:
#         return num_list[0] + list_sum(num_list[1:])
#
# print(list_sum(num_list = [1,3,5,7,9,11,13]))

# 用递归将整数转换成以2-16为进制基数的字符串
# def to_str(n, base):
#     convert_string = "0123456789ABCDEF"
#     if n < base:
#         return convert_string[n]
#     else:
#         return to_str(n // base, base) + convert_string[n % base]
# print(to_str(10, 2))

# 栈帧：实现递归
# from pythonds3.basic import Stack
#
# def to_str(n, base):
#     r_stack = Stack()
#     convert_string = "0123456789ABCDEF"
#     while n > 0:
#         if n < base:
#             r_stack.push(convert_string[n])
#         else:
#             r_stack.push(convert_string[n % base])
#         n = n // base
#
#     res = ""
#     while not r_stack.is_empty():
#         res += str(r_stack.pop())
#     return res
#
# print(to_str(46432131, 8))

# 可视化递归：小乌龟运动，绘制螺旋线
# import turtle
# def draw_spiral(my_turtle, line_len):
#     if line_len > 0:
#         my_turtle.forward(line_len)
#         my_turtle.right(90)
#         draw_spiral(my_turtle, line_len - 5)
#
# my_turtle = turtle.Turtle()
# my_win = turtle.Screen()
# draw_spiral(my_turtle=my_turtle, line_len=1000)
# my_win.exitonclick()

# 递归：绘制分形树
import turtle
def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 10, t)
        t.left(40)
        tree(branch_len - 10, t)
        t.right(20)
        t.backward(branch_len)

t = turtle.Turtle()
my_win = turtle.Screen()
t.left(90)
t.up()
t.backward(200)
t.down()
t.color("red")
tree(50, t)