"""
author:guoxu
date:2025-02-18
introduction:删除无序链表中的重复节点
"""
# 方法一，使用哈希集合记录已经出现的节点值，并在遍历链表的过程中删除重复节点。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteduplicates(self, head: ListNode) -> ListNode:
        # set是基于哈希表实现
        seen = set()
        dummy = ListNode(0, head)
        cur = dummy
        # 遍历链表
        while cur.next:
            if cur.next.val in seen:
                # 如果集合中有，就删除该节点
                cur.next = cur.next.next
            else:
                seen.add(cur.next.val)
                cur = cur.next
        
        return dummy.next

