"""
author:guoxu
date:2025-02-19
introduction:有效的括号序列
"""
# 给定一个字符串所表示的括号序列，包含'(',')','[',']','{','}'，判定是否是有效的括号序列
class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        bracket_map = {')':'(', ']':'[', '}':'{'}

        for char in s:
            # 闭括号
            if char in bracket_map:
                # 返回栈顶元素
                top_element = self.stack.pop() if self.stack else '#'
                # 匹配一下看是否对应
                if bracket_map[char] != top_element:
                    return False
            # 开括号
            else:
                self.stack.append[char]
        
        return not self.stack