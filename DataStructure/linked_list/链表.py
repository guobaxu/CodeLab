"""
author:guoxu
date:2025-02-20
introduction: 
"""
'''
链表相关的核心点:
null/nil 异常处理
dummy node 哑巴节点
快慢指针
插入一个节点到排序链表
从一个链表中移除一个节点
翻转链表
合并两个链表
找到链表的中间节点
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# remove-duplicates-from-sorted-list
class Solution:
    def deleteduplicates(self, head: ListNode)->ListNode:
        # 虚拟头节点
        # 可以不用单独讨论head is None的情况
        dummy = ListNode(-111, head)
        cur = dummy

        while cur and cur.next:
            if cur.val ==cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
            pass
        return dummy.next

# remove-duplicates-from-sorted-list-ii
# 遍历查找，时间复杂度是O(N)，虽然使用了while嵌套while，但第二个while遍历过的节点，第一个while不会再遍历
# 节点
class Solution:
    def deleteduplicates(self, head: ListNode)->ListNode:
        dummy = ListNode(-111, head)
        prev, cur = dummy, head

        while cur:
            # 如果当前节点有重复
            if cur.next and cur.val == cur.next.val:
                # 跳过所有重复的节点
                duplicate_val = cur.val
                while cur and cur.val == duplicate_val:
                    cur = cur.next
                # 移动prev
                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy.next

# reverse-linked-list
class Solution:
    # 思路一：设置前置节点pre，注意链接断开的时机
    def reversList(self, head: ListNode)->ListNode:
        pre = None
        cur = head

        while cur:
            temp_node = cur.next
            cur.next = pre
            pre = cur
            cur = temp_node
        return pre
    
    # 思路二：递归思想
    def recursive(self, head: ListNode)->ListNode:
        # 假设经过recursive返回的listnode已经逆序
        # 边界条件
        if head is None or head.next is None:
            return head
        # 递归函数中传入的就是减少状态的链表，该状态逼近边界条件
        # 返回的节点是新的头节点，递归栈的最底层就是边界条件中返回的head
        rev_head = self.reverseList(head.next)
        # 此时我们处于最外层，也即只剩一个节点未逆转
        head.next.next = head
        head.next = None

        return rev_head