class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 后序遍历非递归
class Solution:
    def postorderTraversal(self, root:Node):
        if not root:
            return []
        s, postorder = [], []
        node, last_visited = root, None

        while len(s)>0 or node is not None:
            if node is not None:
                s.append(node)
                node = node.left
            else:
                peek = s[-1]
                if peek.right is not None and last_visited != peek.right:
                    node = peek.right
                else:
                    last_visited = s.pop()
                    postorder.append(last_visited.value)
        
        return postorder
    
# 判断一棵二叉树是否平衡
class Solution:
    def isBalanced(self, root: Node) -> bool:
        if root is None:
            return True
        # 栈中元素：当前节点、左子树深度、右子树深度
        s  = [[Node(0), -1, -1]]
        node, last_visited = root, None
        while len(s)>1 or node is not None:
            if node is not None:
                s.append([node, -1, -1])
                node = node.left
                if node is None:
                    s[-1][1] = 0
            else:
                peek = s[-1][0]
                if peek.right is not None and last_visited != peek.right:
                    node = peek.right
                else:
                    if peek.right is None:
                        s[-1][2] = 0
                    last, ld, rd = s.pop()
                    if abs(ld - rd) > 1:
                        return False
                    d = max(ld, rd) + 1
                    # 把当前节点的深度更新到父节点
                    # 现在栈顶一定是父节点，兄弟节点会pop掉
                    if s[-1][1] == -1:
                        s[-1][1] = d
                    else:
                        s[-1][2] = d
        return True