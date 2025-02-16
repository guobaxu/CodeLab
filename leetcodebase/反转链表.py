"""
author:guoxu
date:2025-02-16
introduction:反转链表
"""
# leetcode题
# 206.反转链表
class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode)-> ListNode:
        # 初始化前置节点为none, 当前节点为头节点
        pre = None
        cur = head
        while cur:
            # 保存下一个节点
            next_node = cur.next
            # 下面放心对当前节点curr操作，可以操作指针了
            # 反转指针
            cur.next = pre
            # 移动pre和cur的位置
            pre = cur
            cur = next_node
        return pre

# 注意节点可以被访问的方式
# 要么是通过node.next，要么就是直接存储node，
# 总之操作链表时，贸然中断指针，会访问不到之后的节点