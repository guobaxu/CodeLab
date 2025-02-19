"""
author:guoxu
date:2025-02-19
introduction:逆序一个栈
"""
# 递归的方法
# 双递归方法
class Solution:
    def reverseStack(self, stack):
        if not stack:
            return

        # 取出栈顶元素
        top = stack.pop()
        # 定义reverseStack实现逆序栈的作用
        self.reverseStack(stack)

        # 将取出的元素插入到逆序后的栈底
        self.insertbottom(stack, top)

    def insertbottom(self, stack, val):
        if not stack:
            # 栈空直接入栈
            stack.append(val)
            return
        # 递归地取出栈顶元素(状态变化操作)
        top = stack.pop()
        self.insertbottom(stack, val)
        # 将取出的元素重新推入栈中
        stack.appen(top)
