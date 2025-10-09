"""
author:guoxu
date:2025-02-20
introduction:介绍一下语言技巧
"""
# 参考https://github.com/dashidhy/algorithm-pattern-python/blob/master/introduction/python.md

'''
数组特点和技巧
'''
# 数组初始化
# 初始化一个长度为 N 的一维数组
N = 10
M = 10
Array = [0] * N
# 初始化一个形状为 MxN 的二维数组(矩阵)
Matrix = [[0] * N for _ in range(M)] # 思考：可以写成 [[0] * N] * M 吗？
Matrix2 = [[0] * N] * M # 也可以

list.index()    # 返回第一个匹配元素的索引，元素必须在list内


'''
在 Python 中，a, b = b, a是一种 ​​优雅且高效​​ 的变量交换方式，它可以在 ​​不借助临时变量​​ 的情况下交换两个变量的值。
它的底层实现元组解包Tuple Unpacking
'''
a, b, c = 1,2,3
# python风格交换元素值
a, b = b, a
#等效代码
temp_tuple = (b, a)  # 先计算右侧，生成元组
a, b = temp_tuple     # 再解包赋值


# 判断 a，b，c 是否相等，Python里可以直接写连等
if a == b == c:
    True

# 不等式也可以
if a <= b < c:
    True

'''
标准算法
'''
# 排序
# Python 中排序主要使用 sorted() 和 .sort() 函数
# list.sort()原地排序
a = [5,1,6,8,2]
a.sort()
# sorted()是函数，可对iterable排序生成一个list
sort_list = sorted([5,1,6,8,2])

# 参数key
sorted("This is a test string from Andrew".split(), key=str.casefold)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# 二分查找和插入
# bisect模块用于在已排序的列表中高效地插入元素或查找元素的插入位置。它基于二分查找算法，适用于维护有序列表。
import bisect
# 已排序的列表
data = [1, 3, 4, 4, 6, 8]

# 查找插入位置
index_left = bisect.bisect_left(data, 4)  # 返回 2（第一个 >= 4 的位置）
index_right = bisect.bisect_right(data, 4)  # 返回 4（第一个 > 4 的位置）
# 插入元素
bisect.insort_left(data, 5)  # 插入到第一个 >= 5 的位置
bisect.insort_right(data, 4)  # 插入到第一个 > 4 的位置
# 插入后的列表: [1, 3, 4, 4, 4, 5, 6, 8]

'''
标准数据结构
'''
# 栈 Using Lists as Stacks LIFO
stack = [3, 4, 5]
stack.append(6)
stack.pop()

# 队列 Using Lists as Queues FIFO
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.popleft()                 # The first to arrive now leaves

# 堆
# Python 中没有真的 heap 类，实现堆是使用 list 类配合 heapq 库中的堆算法，
# 且只支持最小堆，最大堆需要通过传入负的优先级来实现，

# HashSet，HashTable
# 分别通过 set 类和 dict 类来实现。

'''
collections 库
Python 的 collections 库在刷题时会经常用到，它拓展了一些Python中基础的类，提供了更多功能，
例如 defaultdict 可以预设字典中元素 value 的类型，自动提供初始化，Counter 可以直接统计元素出现个数等。
'''

'''
Python 的三元表达式（x if condition else y）是一种简洁的条件赋值方式，相比传统的 if-else语句，它在 ​​代码简洁性、可读性和功能性​​ 上有显著优势。
'''
condition = True
if condition:
    result =  True
else:
    result = False

# 三元表达式
result = True if condition else False

#三元表达式可以与 lambda、map、filter等结合使用：
# 使用三元表达式与 lambda 结合
func = lambda x: "Even" if x % 2 == 0 else "Odd"
# 使用三元表达式与 map 结合
numbers = [1, 2, 3, 4, 5]
mapped = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", numbers))
# 使用三元表达式与 filter 结合
filtered = list(filter(lambda x: "Even" if x % 2 == 0 else False, numbers))
# 使用三元表达式与列表推导式结合
filtered_list = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

'''
常用内建函数
'''
# max(iterable, key=func),前者是可迭代对象，后者是可选的函数名
from collections import Counter
nums = [1, 2, 3, 2, 1, 4, 5, 5]
counts = Counter(nums)
max(counts.keys(), key=counts.get)


'''
python 中的 collections 模块
collections是 Python 标准库中提供的高性能容器数据类型模块，
扩展了内置容器（list、dict、set、tuple）的功能。
'''
