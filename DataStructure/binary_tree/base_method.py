"""
author:guoxu
date:2025-04-06
introduction: 
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

# preorder traverse
class preorder_traverse:
    def Solution(self, root: TreeNode) -> list:
        preorder = []
        if not root:
            return preorder
        s = [root]
        while len(s) > 0:
            node = s.pop()
            preorder.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return preorder
    

# inorder traverse
# store a visit tag
class inorder_traverse:
    def Solution(self, root:TreeNode) -> list:
        inorder, s = [], []
        node = root
        while len(s)>0 or node is not None:
            if node:
                s.append(node)
                node = node.left
            else:# when left child is none, back to parrent
                node = s.pop()
                inorder.append(node.val)
                node = node.right
        return inorder

# postorder traverse
# 核心思路：左子树 -> 右子树 -> 根节点
# 1.不断向左子树深入​​，直到 node 为 None（即左子树遍历完毕）。
# 2.检查栈顶节点（peek）的右子树：
# * 如果右子树​​存在且未被访问过lastvisit != peek.right，则访问右子树
# * 如果右子树​​不存在，或者右子树已经被访问过，则说明当前节点的左右子树均已处理完毕，可以访问该节点（即 peek），并将其从栈中弹出
class postorder_traverse:
    def Solution(self, root: TreeNode) -> list:
        postorder, s = [], []
        lastvisit = None
        node = root
        while len(s)>0 or node is not None:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                peek = s[-1]
                if peek.right is not None and lastvisit != peek.right:
                    node = peek.right
                else:
                    lastvisit = s.pop()
                    postorder.append(node.val)
        return postorder

# DFS从下到上，分治法
# 后序遍历思想，递归方法
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        # boundary condition
        if root is None:
            return []
        # divide two sub-problems
        left_result = self.preorderTraversal(root.left)
        right_result = self.preorderTraversal(root.right)

        return [root.val] + left_result + right_result

from collections import deque
# 层次遍历模板
class Solution:
    def levelorder(self, root:TreeNode):
        levels = []
        if root is None:
            return levels
        # core: level order queue
        bfs = deque([])
        while len(bfs)>0:
            """
            operate
            """
            levels.append([])
            # core: enqueue
            level_size = len(bfs)
            for _ in range(level_size):
                node = bfs.popleft()
                if node.left is not None:
                    bfs.append(node.left)
                if node.right is not None:
                    bfs.append(node.right)

# balanced-binary-tree
# D&C recursion
# 分治法（从下到上），左子树平衡 && 右子树平衡 && 左右子树高度差 <= 1
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(node):
            if node is None:
                return 0, True
            left_depth, bool_left = depth(node.left)
            right_depth, bool_right = depth(node.right)
            is_balanced = bool_left and bool_right and abs(left_depth-right_depth) <= 1
            return max(left_depth, right_depth) + 1, is_balanced
        _, out = depth(root)
        return out
# 使用后序遍历判断二叉树是否平衡
# 
class Solution:
    def isBalanced_traversal(self, root: TreeNode) -> bool:
        pass
    def postorder_traversal(self, root: TreeNode) -> list:
        postorder, s = [], []
        lastvisit = None
        node = root
        while len(s)>0 or node is not None:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                
                peek = s[-1]
                if peek.right is not None and lastvisit != peek.right:
                    node = peek.right
                else:
                    lastvisit = s.pop()
                    postorder.append(node.val)
        return postorder


# build tree
def build_tree(lst):
    from collections import deque
    if not lst:
        return None
    
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(lst):
        current = queue.popleft()
        
        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    
    return root

if __name__ == "__main__":
    # 示例列表
    lst = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
    root = build_tree(lst)