"""
author:guoxu
date:2025-02-17
introduction:使用链表实现栈和队列
"""
# 使用链表实现栈
# 思想：栈是LIFO，在链表头部插入和删除操作
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    # 入栈
    def push(self, x:int)->None:
        node = ListNode(x)
        node.next = self.top
        self.top = node

    # 出栈
    def pop(self)->int:
        # 空栈处理
        if self.top is None:
            raise IndexError("pop from empty stack")
        value = self.top.val
        self.top = self.top.next
        return value
    
    # 查询栈顶的值
    def peek(self)->int:
        if self.top is None:
            raise IndexError("peek from empty stack")
        return self.top.val

    # 查询是否栈空
    def empty(self)->bool:
        return self.top is None

# 使用链表实现队列
# 思想：队列是FIFO，在链表头部删除，链表尾部插入，需要维护两个指针（front--->node---->rear）
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    # 入队
    def enqueue(self, x:int)->None:
        node = ListNode(x)
        if self.rear is None:
            self.rear = self.front = node
        else:
            self.rear.next = node
            self.rear = node

    # 出队
    def dequeue(self)->int:
        # 从队列头部删除节点，返回值
        if self.front is None:
            raise IndexError("dequeue from empty queue")
        value = self.front.val
        self.front = self.front.next
        # 边界判断
        if self.front is None:
            self.rear = None
        return value

    # 查询队列头部的值
    def peek(self)->int:
        if self.front is None:
            raise IndexError("peek from empty queue")
        return self.front.val

    # 查询是否队列空
    def empty(self)->bool:
        return self.front is None