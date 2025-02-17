"""
author:guoxu
date:2025-02-17
introduction:判断链表是否有环
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hascycle(self, head:ListNode)->bool:
        # 初始化快慢指针
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # 如果快慢指针相遇
            if slow == fast:
                return True
        
        return False

# 如果有环，返回环的起始节点
class Solution:
    def hascycle(self, head:ListNode)->ListNode:
        # 初始化快慢指针
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # 如果快慢指针相遇
            if slow == fast:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow
        
        return None
# 最后相遇之后有个公式a=(n-1)环长+c，
# a指头节点到环起始节点的距离，
# c是快慢指针相遇位置到环起始节点的距离（原来的方向）