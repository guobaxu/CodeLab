"""
author:guoxu
date:2025-02-16
introduction:删除单链表倒数第K个节点
"""
# leetcode题
# 19.删除链表的倒数第N个节点
# 使用两个指针实现，其中一个比另一个指针提前K个节点
# 当前面的指针到达链表尾部时，后面的指针的下一个节点就是需要被删除的节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 虚拟头节点技巧?
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # 将第一个指针向前移动n+1个位置
        for _ in range(n+1):
            first = first.next
        
        # 将两个指针同时移动，直至第一个指针移动到末尾
        while first:
            first = first.next
            second = second.next
        
        # 删除节点的技巧
        second.next = second.next.next

        return head

# 遍历操作，时间复杂度是O(n)，空间复杂度是O(1)