"""
author:guoxu
date:2025-02-17
introduction:删除链表中的节点（要求O(1)时间复杂度）
"""

class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node:ListNode)->None:
        if node.next:
            node.val = node.next.val
            node.next = node.next.next