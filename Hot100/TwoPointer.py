from typing import List


class Solution:
    # 283. 移动零
    # 思路：这是一个数组，维护两个指针，一个代表0元素，一个标识非零元素
    # 下面这个解法使用了循环嵌套，时间复杂度O(N^2)，空间复杂度O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            # 非0元素直接跳过
            if nums[i] is not 0:
                continue
            else:
                # 循环找到当前index之后的第一个非0元素
                to_exchage = i
                while to_exchage < len(nums) and nums[to_exchage] == 0:
                    to_exchage += 1
                if to_exchage == len(nums):
                    # 剩余元素都是0
                    break
                nums[i], nums[to_exchage] = nums[to_exchage], nums[i]
    # 快慢指针
    # 快指针 (fast/cur)： 负责探路，寻找非0元素。
    # 慢指针 (slow/dest)： 代表“非0元素应该放置的下一个位置”。
    def moveZeroes_fast_slow(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            # 识别信号：找到非0元素
            if nums[fast] != 0:
                # 业务逻辑：把它交换到 slow 的位置
                # 只有当 fast > slow 时才需要交换 (避免自己和自己交换)
                if fast > slow:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
    