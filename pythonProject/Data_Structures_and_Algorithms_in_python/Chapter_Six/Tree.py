# my_tree = ['a',
#            ['b', ['d', [], []], ['e', [], []]],
#            ['c', ['f', [], []]]
#             ]
#
# print(my_tree)
# print(my_tree[0])
# print(my_tree[1])
# print(my_tree[1][1])
# print(my_tree[1][2])
# print(my_tree[2])
# print(my_tree[2][0])
# print(my_tree[2][1])

#以列表之列表构建二叉树
# def make_binary_tree(root):
#     return [root, [], []]
#
# # 插入左子树
# def insert_left(root, new_child):
#     old_child = root.pop(1)
#     if len(old_child) > 1:
#         root.insert(1, [new_child, old_child, []])
#     else:
#         root.insert(1, [new_child, [], []])
#     return root
#
# # 插入右子树
# def insert_right(root, new_child):
#     old_child = root.pop(2)
#     if len(old_child) > 1:
#         root.insert(2, [new_child, [], old_child])
#     else:
#         root.insert(2, [new_child, [], []])
#     return root
#
#  # 树的访问函数
# def get_root_val(root):
#     return root[0]
#
# def set_root_val(root, new_val):
#     root[0] = new_val
#
# def get_left_child(root):
#     return root[1]
#
# def get_right_child(root):
#     return root[2]
#
# a_tree = make_binary_tree(3)
# print(a_tree)
# print(insert_left(a_tree, 4))
# print(insert_left(a_tree, 5))
# print(insert_right(a_tree, 6))
# print(insert_right(a_tree, 7))
# print(get_left_child(a_tree))
# print(get_right_child(a_tree))
# set_root_val(get_left_child(a_tree), 9)
# print(a_tree)
# print(insert_left(get_left_child(a_tree), 11))
# print(a_tree)
# print(get_right_child(insert_right(a_tree, 12)))
# print(a_tree)
# print(get_right_child(get_right_child(a_tree)))

# 节点与引用
# class BinaryTree:
#     def __init__(self, root_obj):
#         self.key = root_obj
#         self.left_child = None
#         self.right_child = None
#
#     def insert_left(self, new_node):
#         if self.left_child is None:
#             self.left_child = BinaryTree(new_node)
#         else:
#             new_child = BinaryTree(new_node)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#
#     def insert_right(self, new_node):
#         if self.right_child is None:
#             self.right_child = BinaryTree(new_node)
#         else:
#             new_child = BinaryTree(new_node)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#
#     def get_root_val(self):
#         return self.key
#
#     def set_root_val(self, new_obj):
#         self.key = new_obj
#
#     def get_left_child(self):
#         return self.left_child
#
#     def get_right_child(self):
#         return self.right_child
#
# a_tree = BinaryTree('a')
# print(a_tree.get_root_val())
# print(a_tree.get_left_child())
# a_tree.insert_left('b')
# print(a_tree.get_left_child().get_root_val())
# a_tree.insert_right('c')
# print(a_tree.get_right_child().get_root_val())
# a_tree.get_right_child().set_root_val('Hello')
# print(a_tree.get_right_child().get_root_val())

# 解析树构建器
# from pythonds3.basic import Stack
# from pythonds3.trees import BinaryTree
#
# def build_parse_tree(fp_exp):
#     fp_list = fp_exp.split()
#     p_stack = Stack()
#     expr_tree = BinaryTree("")
#     p_stack.push(expr_tree)
#     current_tree = expr_tree
#
#     for i in fp_list:
#         if i == '(':
#             current_tree.insert_left("")
#             p_stack.push(current_tree)
#             current_tree = current_tree.left_child
#         elif i in ["+", "-", "*", "/"]:
#             current_tree.root = i
#             current_tree.insert_right("")
#             current_tree = current_tree.right_child
#         elif i.isdigit():
#             current_tree.root = int(i)
#             parent = p_stack.pop()
#             current_tree = parent
#         elif i == ")":
#             current_tree = p_stack.pop()
#         else:
#             raise ValueError(f"Unknown operator '{i}'")
#     return expr_tree
#
# # 计算二叉解析树的递归函数
# import operator
# def evaluate(parse_tree):
#     operators = {
#         "+": operator.add,
#         "-": operator.sub,
#         "*": operator.mul,
#         "/": operator.truediv,
#     }
#     left_child = parse_tree.left_child
#     right_child = parse_tree.right_child
#
#     if left_child and right_child:
#         fn = operators[parse_tree.root]
#         return fn(evaluate(left_child), evaluate(right_child))
#     else:
#         return parse_tree.root

# 二叉堆
from pythonds3.trees import BinaryHeap
my_heap = BinaryHeap()
my_heap.insert(5)
my_heap.insert(7)
my_heap.insert(3)
my_heap.insert(11)
print(my_heap)
print(my_heap.delete())
print(my_heap)
print(my_heap.delete())
print(my_heap)
print(my_heap.delete())
print(my_heap)