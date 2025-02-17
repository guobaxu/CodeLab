"""
author:guoxu
date:2025-02-17
introduction:打印两个链表的公共部分
"""
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def print_common_part(self, head1:ListNode, head2:ListNode):
        cur1 = head1
        cur2 = head2

        # 遍历两个链表
        while cur1 is not None and cur2 is not None:
            if cur1.value < cur2.value:
                cur1 = cur1.next
            elif cur1.value > cur2.value:
                cur2 = cur2.next
            else:
                print(cur1.value, end=" ")
                cur1 = cur1.next
                cur2 = cur2.next