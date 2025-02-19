"""
author:guoxu
date:2025-02-19
introduction:字符串匹配
"""
# leetcode:28. 找出字符串中第一个匹配项的下标
class Solution:
    def searchstr(self, source: str, target: str) -> int:
        n, m = len(source), len(target)
        
        if m == 0:
            return 0

        for i in range(n-m+1):
            if source[i:i+m] == target:
                return i
        return -1
