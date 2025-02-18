"""
author:guoxu
date:2025-02-18
introduction:向有序环形链表中加入新的节点
"""
# 环形链表是最后一个节点指向头节点。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: ListNode, insertVal: int) -> ListNode:
        new_node = ListNode(insertVal)

        if not head:
            new_node.next = new_node
            return new_node
        
        pre, cur = head, head.next
        to_insert = False

        while True:
            # 情况1：插入节点的值位于pre和cur之间
            if pre.val <= insertVal <= cur.val:
                to_insert = True
            #情况2：当前节点是最大节点，下一节点是最小节点，插入节点的值大于最大节点或小于最小节点
            elif pre.val > cur.val:
                if insertVal >= pre.val or insertVal <= cur.val:
                    to_insert = True
            
            if to_insert:
                pre.next = new_node
                new_node.next = cur
                return head
            
            pre, cur = cur, cur.next
            # 遍历一圈回到head，仍未插入节点，就直接插入在起点之前
            if pre == head:
                break
        pre.next = new_node
        new_node.next = cur
        return head