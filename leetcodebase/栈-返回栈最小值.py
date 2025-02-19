"""
author:guoxu
date:2025-02-19
introduction:实现一个取最小值方法的栈
"""
# 实现的栈将支持push，pop和min操作，所有操作要求都在O(1)时间内完成。
# 可以使用两个栈，一个用于存储所有元素，一个用于存储当前的最小值
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, x:int)->None:
        self.stack.append[x]
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self)->None:
        if self.stack:
            top = self.stack.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self)->int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("stack is empty")

    def getMin(self)->int:
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("min_stack is empty")
        