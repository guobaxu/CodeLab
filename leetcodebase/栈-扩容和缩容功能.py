"""
author:guoxu
date:2025-02-19
introduction:使用数组实现一个栈，提供自动扩容和缩容功能
"""
# 栈满时，数组容量加倍；栈小于容量四分之一时，数组容量减半
# 时间复杂度O(1)均摊?
# 在大多数情况下，入栈和出栈都是O(1)，当需要扩容和缩容时是O(n)，但扩容和缩容都是偶尔发生的，
class ArrayStack:
    def __init__(self,capacity):
        # 初始化栈，初始容量为2
        self.stack = [None]*capacity
        self.capacity = capacity
        self.size = 0

    def push(self, x):
        # 如果栈满了，自动扩容
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.stack[self.size] = x
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            raise IndexError("pop from empty stack")
        x = self.stack[self.size - 1]
        self.stack[self.size - 1] = None
        self.size -= 1
        # 如果栈的大小小于容量的四分之一，则进行缩容
        if 0 < self.size == self.capacity // 4:
            self._resize(self.capacity//2)
        return x
    
    def peek(self):
        if self.size == 0:
            raise IndexError("peek from empty stack")
        return self.stack[self.size - 1]

    # 内部方法
    def _resize(self, new_capacity):
        # 调整数组大小
        new_stack = [None] * new_capacity
        for i in range(self.size):
            new_stack[i] = self.stack[i]
        self.stack = new_stack
        self.capacity = new_capacity

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    