# leetcode:389. 找不同


# 方法思路：​​异或（XOR）运算​​
# 异或运算（^）有以下重要性质：
# ​​交换律​​：a ^ b ^ c = a ^ c ^ b
# ​​结合律​​：(a ^ b) ^ c = a ^ (b ^ c)
# ​​自反性​​：a ^ a = 0（相同数异或结果为 0）
# ​​与 0 异或​​：a ^ 0 = a
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
         # 初始化异或结果变量为0
        xor = 0
        
        # 遍历字符串s中的每个字符
        for char in s:
            # 将字符转换为ASCII码值进行异或运算
            xor ^= ord(char)
        
        # 遍历字符串t中的每个字符
        for char in t:
            # 将字符转换为ASCII码值进行异或运算
            xor ^= ord(char)
        
        # 最终异或结果是添加字母的ASCII码，转换为字符返回
        return chr(xor)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 维护一个字典，记录s中字符出现的次数
        # 遍历t中的字符，如果不在字典中，就return，存在就减次数
        str_counts_dit = {}
        for i in s:
            if i in str_counts_dit:
                str_counts_dit[i] += 1
            else:
                str_counts_dit[i] = 1
        
        for j in t:
            if str_counts_dit.get(j) is not None:
                str_counts_dit[j] -= 1
                if str_counts_dit[j] < 0:
                    return j
            else:
                return j
                
        # 另一种更简单的方式是，直接遍历t中的字符，使用in判断是否在s中
        # 这种不能判断出重复的字符如s='a',t='aa'
        # for i in t:
        #     if i not in s:
        #         return i