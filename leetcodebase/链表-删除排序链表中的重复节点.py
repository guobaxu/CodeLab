"""
author:guoxu
date:2025-02-18
introduction:删除有序链表中的重复节点
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 注意虚拟头节点的值要和head的值区分开，避免一样
        dummy = ListNode(0, head)
        cur = dummy

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head