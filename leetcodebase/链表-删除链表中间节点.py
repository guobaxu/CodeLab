"""
author:guoxu
date:2025-02-17
introduction:删除链表中间节点
"""
# 思想：使用快慢指针，慢指针每走一步，快指针就走两步
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deletemiddle(self, head:ListNode) -> ListNode:
        # 边界判断，只有一个节点或空
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        # 用于链接被删除节点前后
        pre = None

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        pre.next = slow.next

        return head