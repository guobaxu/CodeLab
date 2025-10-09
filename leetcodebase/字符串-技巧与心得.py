
# ASCII码是 ​7 位二进制数（0~127）​​ 表示字符
# 大小写字母的ASCII码范围是65-90（大写）和97-122（小写）
# 字符 → ASCII 码
ord('A')  # 输出 65

# ASCII 码 → 字符
chr(65)   # 输出 'A'

char = 'a'
if 97 <= ord(char) <= 122:
    print("小写字母")


# 字符串不好操作，可以将其转化为列表
s = "hello"
s_list = list(s)  # ['h', 'e', 'l', 'l', 'o']
# 列表有反转函数,in-place翻转
s_list.reverse()  # ['o', 'l', 'l', 'e', 'h']
print(s_list.reverse())
"""
Do not return anything, modify s in-place instead.
"""
left = 0
right = len(s_list) - 1
while left < right:
    s_list[left], s_list[right] = s_list[right], s_list[left]
    left += 1
    right -= 1


# 不要用+拼接字符串，要用''.join拼接
# 不推荐
result = ""
for s in ["a", "b", "c"]:
    result += s  # 每次拼接生成新字符串

# 推荐
parts = ["a", "b", "c"]
result = "".join(parts)  # 一次性拼接