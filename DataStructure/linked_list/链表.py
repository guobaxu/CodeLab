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
    # 至少维护三个节点变量，确保操作cur节点的时候存储其前后两个节点
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

# reverse-linked-list 2
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # bondary condition
        if not head.next:
            return head
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        index = 0
        left -= 1
        right -= 1

        while cur:
            print("node val: ",cur.val)
            # interval judge and reverse link list
            if left <= index <=right:
                if index == left:
                    # preserve prenode
                    pre_node = pre
                    print("pre_node val:{}, next node val {}".format(pre_node.val, pre_node.next.val))
                while left <= index <=right:
                    print("index:", index)
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                    index += 1
                else:
                    pre_node.next.next = cur
                    pre_node.next = pre
            else:
                pre = cur
                cur = cur.next
                index += 1
        return dummy.next

# merge two sorted lists
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        tail = dummy = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

# partition list
class Solution:
    def partitionlist(self, head:ListNode, x:int) -> ListNode:
        dummy = ListNode(next=head)
        pre, cur = dummy, head
        high_val_list = ListNode(0)
        high_cur = high_val_list
        while cur:
            if cur.val >= x:
                # add to high list
                high_cur.next = cur
                high_cur = high_cur.next
                # cur move
                temp = cur.next
                cur.next = None
                cur = temp
                pre.next = cur
            else:
                pre = cur
                cur = cur.next

        pre.next = high_val_list.next
        return dummy.next

# sort list
class Solution:
    def sortList(self, head:ListNode) -> ListNode:
        # boundry condition
        if not head or not head.next:
            return head
        
        # find middle node
        mid_node = self.find_mid(head)
        rightlist = mid_node.next
        mid_node.next = None

        # merge
        return self.merge_and_sort(self.sortList(head), self.sortList(rightlist))
    
    def find_mid(self,start:ListNode) -> ListNode:
        # fast and slow pointer
        slow, fast = start, start.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def merge_and_sort(self, left:ListNode, right:ListNode) -> ListNode:
        # suppose left list and right list are both sorted list
        # merge left list and right list to one sort list
        tail = dummy = ListNode(0)
        while left and right:
            if left.val <= right.val:
                tail.next = left
                tail = tail.next
                left = left.next
            else:
                tail.next = right
                tail = tail.next
                right = right.next
        
        if left:
            tail.next = left
        elif right:
            tail.next = right
        return dummy.next
    
    def sortList_uselistmethod(self, head:ListNode) -> ListNode:
        # boundry condition
        if not head or not head.next:
            return head
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        # use sort method with lambda function
        nodes.sort(key=lambda x: x.val)
        cur = ListNode(0)
        for node in nodes:
            cur.next = node
            cur = cur.next
        nodes[-1].next = None
        return nodes[0]

# reorder List
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        # find mid node
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid_node = slow.next
        slow.next
        # reverse half lsit
        r = self.reverseLsit(mid_node)
        l = head
        while l and r:
            temp = r.next
            r.next = l.next
            l.next = r
            l = l.next.next
            r = temp
        return

    def reverseLsit(self, head:ListNode)->ListNode:
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

# linked-list-cycle
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # slow and fast pointer
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False


# linked-list-cycle-ii
class Solution:
    def hasCycle(self, head: ListNode) -> ListNode:
        # slow and fast pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # fast first meet slow in cycle
            if slow is fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                else:
                    return slow
        else:
            return None

# palindrome-linked-list
# 使用快慢指针找到中点，同时记录slow经过的节点值，再遍历后半部分的链表对比
# 或者直接一个list记录所有的节点值，再使用for索引做比较
# 时间复杂度O(N)，但空间复杂的也是O(N)
# 如果想要空间复杂度是O(1)，则找到中点，对后半部分反转
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        all_val = []
        # store all node val
        while slow:
            all_val.append(slow.val)
            slow = slow.next
        length = len(all_val)
        for i in range(0,length//2):
            if all_val[i] != all_val[length-1-i]:
                return False
        return True

# deepcopyRandomList

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        cur = head
        mapping = {}

        # first traverse to stroe val
        while cur:
            # create new node with same val
            mapping[cur] = Node(cur.val)
            cur = cur.next
        # secend traverse to build pointer
        cur = head
        while cur:
            if cur.next:
                mapping[cur].next = mapping[cur.next]
            if cur.random:
                mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]


if __name__ == "__main__":
    nodeval = [1,4,3,2,5,2]
    dummy = ListNode(0)
    cur = ListNode(0)
    dummy.next = cur
    for i in nodeval:
        node = ListNode(i)
        cur.next = node
        cur = node
    head = dummy.next.next
    # while cur:
    #     print(cur.val)
    #     cur = cur.next


    solution = Solution()
    revesed_head = solution.partitionlist(head, x=3)
    while revesed_head:
        print(revesed_head.val)
        revesed_head = revesed_head.next

    