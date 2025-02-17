"""
author:guoxu
date:2025-02-16
introduction:删除链表中给定值的节点
"""
# leetcode题：
# 237. 删除链表中的节点
# 1325. 删除给定值的叶子节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def deleteNode(self, head:ListNode, val:int) -> ListNode:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 虚拟头节点技巧
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        pre = dummy
        # 遍历找到需要被删除的节点位置
        while cur and cur.val != val:
            pre = cur
            cur = cur.next
        # 删除节点操作
        pre.next = cur.next
        # 返回
        return dummy.next
    def removeLeafNodes(self, head: ListNode, val: int) -> ListNode:
        # 虚拟头节点技巧
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        # 遍历
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next