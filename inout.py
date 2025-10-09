

# # 赛码网输入输出
# # 单个输入，单个输出
# inputint = int(input())
# output = inputint
# print(str(output))

# # 单行多个输入，单行多个输出，空格分割（多行输入，每一行是一个测试样例）
# inputs = list(map(int, input().split(" ")))
# m, n = inputs[0], inputs[1]
# print(str(m), str(n))

# # 多个测试案例，每个测试案例多行
# while 1:
#     nm = list(map(int,input().split(" ")))

#     N = nm[0]
#     M = nm[1]
#     print(str(N)+' '+str(M))
#     for i in range(M):
#         abc = list(map(int, input().split(" ")))
#         a, b, c = abc[0], abc[1], abc[2]
#         print(str(a)+' '+str(b)+' '+str(c))


# 牛客网输入输出
# 多行输入，每一行是一个测试样例
# import sys 
# for line in sys.stdin:
#     a = line.split(" ")
#     print(a[0],a[1])

# 多个测试用例，每个测试用例有多行
# 输入包含多组测试用例。对于每组测试用例：第一行包含两个整数N和M，在接下来的M行内，每行包括3个整数。要求按照输入格式输出。
import sys
for line in sys.stdin:
    n, m = map(int, line.strip(" "))
    print("测试用例", n, m)
    for i in range(m):
        for line in sys.stdin:
            a, b, c = map(int, line.strip(" "))
            print("三个整数", a, b, c)

# 输入
# 3 1
# 2 3 1
# 5 4
# 1 2 1
# 3 4 0
# 2 5 1
# 3 2 1

# ==================== 常用输入输出模式总结 ====================

# 1. 基础输入方式
print("=== 1. 基础输入方式 ===")
# 单个整数
n = int(input())

# 单个字符串  
s = input()

# 单行多个整数（空格分隔）
a, b, c = map(int, input().split())

# 单行多个整数（列表形式）
nums = list(map(int, input().split()))

# 2. 多行输入模式
print("=== 2. 多行输入模式 ===")
# 已知行数的多行输入
n = int(input())
for i in range(n):
    line = input().split()
    print(line)

# 3. 文件输入输出
print("=== 3. 文件输入输出 ===")
# 从文件读取
with open('input.txt', 'r') as f:
    lines = f.readlines()

# 写入文件
with open('output.txt', 'w') as f:
    f.write("结果")

# 4. 标准输入输出（适合在线判题）
print("=== 4. 标准输入输出 ===")
# 使用sys.stdin（适合大数据量）
import sys
for line in sys.stdin:
    data = line.strip().split()
    print(data)

# 5. 常见数据结构输入
print("=== 5. 常见数据结构输入 ===")
# 二维数组输入
n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# 图输入（邻接表）
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 无向图

# 6. 特殊输入格式
print("=== 6. 特殊输入格式 ===")
# 逗号分隔
nums = list(map(int, input().split(',')))

# 多行字符串
n = int(input())
strings = [input().strip() for _ in range(n)]

# 7. 输出格式
print("=== 7. 输出格式 ===")
result = [1, 2, 3]
# 空格分隔输出
print(' '.join(map(str, result)))

# 换行分隔输出
for item in result:
    print(item)

# 格式化输出
print(f"Case {i}: {result}")

# 8. 在线判题平台常用模式
print("=== 8. 在线判题平台常用模式 ===")

# LeetCode模式（函数参数）
def solution(nums):
    return result

# 牛客网模式
# import sys
for line in sys.stdin:
    a, b = map(int, line.strip().split())
    print(a + b)

# 赛码网模式
while True:
    try:
        n = int(input())
        print(n)
    except:
        break

# 9. 性能优化技巧
print("=== 9. 性能优化技巧 ===")
# 使用sys.stdin.readline()代替input()
import sys
input = sys.stdin.readline

# 预读所有输入
import sys
lines = sys.stdin.readlines()

'''
sys.stdin.readline(): 更快，直接调用系统底层读取函数, 手动处理换行符：line.strip()
input(): 较慢，内部会调用 sys.stdin.readline() 并额外处理换行符
'''

# 10. 错误处理
print("=== 10. 错误处理 ===")
# try-except处理输入结束
while True:
    try:
        n = int(input())
        print(n)
    except EOFError:
        break
    except:
        break
