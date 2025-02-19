"""
author:guoxu
date:2025-02-19
introduction:两个队列实现栈
"""
from collections import deque

# 维护一个空队列，新元素加入空队列，然后将另一个队列中的所有元素依次入队
class MyStack:
    def __init__(self):
        self.queue1 = deque()
        # 维护queue2一直为空队列
        self.queue2 = deque()
    
    def push(self,x:int)->None:
        # 将新元素加入到空的queue2中
        self.queue2.append(x)
        # 将queue1的所有元素移到queue2中
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        # 交换queue1和queue2
        self.queue1, self.queue2 = self.queue2, self.queue1
    
    def pop(self)->int:
        # 从queue1中弹出元素，栈顶元素
        if self.queue1:
            return self.queue1.popleft()
        else:
            raise IndexError("pop from empty stack")
    
    def top(self)->int:
        # 返回queue1的队首元素，即
        if self.queue1:
            return self.queue1[0]
        else:
            raise IndexError("top from empty stack")
    
    def empty(self) -> bool:
        return not self.queue1