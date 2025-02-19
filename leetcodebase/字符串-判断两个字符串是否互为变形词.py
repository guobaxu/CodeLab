"""
author:guoxu
date:2025-02-18
introduction:判断两个字符串是否互为变形词
"""
# 互为变形词的条件是两个字符串包含的字符以及每个字符出现的次数相同。
class Solution:
    def isDeformation(self, str1: str, str2: str) -> bool:
        # 如果两个字符串长度不相等，直接返回False
        if len(str1) != len(str2):
            return False

        count = {}

        for char in str1:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        for char in str2:
            if char in count:
                count[char] -= 1
                if count[char] < 0:
                    return False
            else:
                return False
        
        for value in count.values():
            if value != 0:
                return False
        
        return True