class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        # 不使用虚拟头节点
        # # 边界判断，只有一个节点或空
        # if not head or not head.next:
        #     return None
        dummy = ListNode(0, head)
        pre = dummy
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next

        pre.next = slow.next

        return dummy.next 