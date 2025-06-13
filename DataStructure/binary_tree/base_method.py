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

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 使用float('-inf')是因为节点值有负数
        self.maxpath = float('-inf')
        # 递归函数实现返回当前节点的最大路径和
        def lagest_path_at(node):
            # 边界条件
            if node is None:
                return float('-inf')
            # 递归获取左右子树的最大路径和
            P_left = lagest_path_at(node.left)
            P_right = lagest_path_at(node.right)
            # 更新全局最大路径和
            self.maxpath = max(self.maxpath, node.val + max(P_left,0) + max(P_right,0), P_left, P_right)
            return node.val + max(P_left, P_right, 0)
        lagest_path_at(root)
        return self.maxpath



# binary-tree-zigzag-level-order-traversal
# 思路：在BFS迭代模板上改用双端队列控制输出顺序，使用一个switch控制队列pop的方向
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        levels = []
        if root is None:
            return levels
        bfs = deque([root])
        pop_form_left = True
        while len(bfs) > 0:
            levels.append([])
            level_size = len(bfs)
            if pop_form_left:
                for _ in range(level_size):
                    node = bfs.popleft()
                    levels[-1].append(node.val)
                    if node.left is not None:
                        bfs.append(node.left)
                    if node.right is not None:
                        bfs.append(node.right)
            else:
                for _ in range(level_size):
                    node = bfs.pop()
                    levels[-1].append(node.val)
                    if node.right is not None:
                        bfs.appendleft(node.right)
                    if node.left is not None:
                        bfs.appendleft(node.left)
            pop_form_left = not pop_form_left
            
        return levels

# validate-binary-search-tree
# 思路1：使用中序遍历，判断返回的inorder列表是否有序，无法中途停止
# 思路2：使用分治法，当节点的左子树的最大值小于节点值，且右子树的最小值大于节点值，且左右子树都合法时，说明是二叉搜索树

class Solution:
    def isValidBST(self, root:TreeNode) -> bool:
        if root is None:
            return True
        def valid_min_max(node):
            # boundary condition
            is_valid = True
            if node.left is not None:
                l_isvalid, lmin, lmax = valid_min_max(node.left)
                is_valid = is_valid and (lmax < node.val)
            else:
                l_isvalid, lmin = True, node.val
            
            if node.right is not None:
                r_isvalid, rmin, rmax = valid_min_max(node.right)
                is_valid = is_valid and (rmin > node.val)
            else:
                r_isvalid, rmax = True, node.val

            return is_valid and l_isvalid and r_isvalid, lmin, rmax
        
        return valid_min_max(root)[0]
    
# 分治法代码完善过程，从基本组成到完整分支代码
# 1.基本结构：边界条件，状态变化，当前节点操作
def valid_min_max(node):
    # boundary condition
    if node is None:
        return True, float('inf'), float('inf')
    # subtree
    # 左子树需要返回合法判断和左子树最大值
    l_isvalid, lmax = valid_min_max(node.left)
    # 右子树需要返回合法判断和右子树最小值
    r_isvalid, rmin = valid_min_max(node.right)
    # check current node
    is_valid = l_isvalid and r_isvalid and (lmax < node.val) and (rmin > node.val)
    return is_valid, min(lmax, node.val, rmin), max(lmax, node.val, rmin)
# 2.统一函数返回条件：返回3个值，合法判断，树最小值，树最大值
def valid_min_max(node):
    if node is None:
        return True, float('-inf'), float('inf')
    l_isvalid, lmin, lmax = valid_min_max(node.left)
    r_isvalid, rmin, rmax = valid_min_max(node.right)
    is_valid = l_isvalid and r_isvalid and (lmax < node.val) and (rmin > node.val)
    return is_valid, lmin, rmax

# 3.但空节点的值返回不好控制，改变边界控制，将值检查放在if条件内部
def valid_min_max(node):
    is_valid = True
    # subtree
    if node.left is not None:
        l_isvalid, lmin, lmax = valid_min_max(node.left)
        is_valid = is_valid and (lmax < node.val)
    else:
        l_isvalid, lmin = True, node.val
    if node.right is not None:
        r_isvalid, rmin, rmax = valid_min_max(node.right)
        is_valid = is_valid and (rmin > node.val)
    else:
        r_isvalid, rmax =True, node.val
    return is_valid and l_isvalid and r_isvalid, lmin, rmax





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
    lst = [2,1,3]
    root = build_tree(lst)