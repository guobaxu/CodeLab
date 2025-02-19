"""
author:guoxu
date:2025-02-19
introduction:使用一个辅助栈实现对另一个栈的排序
"""

class Solution:
    def sortstack(self, stack):
        temp_stack = []

        # 遍历原栈中的每个元素
        while stack:
            # 取出原栈的栈顶元素
            current = stack.pop()

            # 左手倒右手
            # 将临时栈中大于current的元素依次弹出并推入原栈
            while temp_stack and temp_stack[-1] > current:
                stack.append(temp_stack.pop())
            
            temp_stack.append(current)
        
        while temp_stack:
            stack.append(temp_stack.pop())

solution = Solution()
stack = [3,5,1,2,7]
solution.sortstack(stack)
print(stack)