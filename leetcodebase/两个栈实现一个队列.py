"""
author:guoxu
date:2025-02-07
introduction:使用两个栈实现一个队列
"""
class MyQueue:
    def __init__(self):
        # 初始化两个栈
        self.stack_in = []  # 用于入队的栈
        self.stack_out = []  # 用于出队的栈

    def push(self, x: int) -> None:
        # 将元素入队，直接压入 stack_in
        self.stack_in.append(x)

    def pop(self) -> int:
        # 出队操作
        # 如果stack_out为空，则将stack_in中的所有元素弹出并堆入stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # 弹出stack_out栈顶元素
        return self.stack_out.pop()

    def peek(self) -> int:
        # 查看队列头部元素
        # 如果stack_out为空，则将stack_in中的所有元素弹出并堆入stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # 弹出stack_out栈顶元素
        return self.stack_out[-1]
    
    def empty(self) -> bool:
        # 检查队列是否为空
        # 当两个栈都为空时，队列为空
        return not self.stack_in and not self.stack_out
