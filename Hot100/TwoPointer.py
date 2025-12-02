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
    
    # 盛最多水的容器
    def maxArea(self, height: List[int]) -> int:
        # 1. 初始化双指针
        left, right = 0, len(height) - 1
        max_area = 0

        # 2. 优化：预先获取最大高度，用于剪枝
        max_h = max(height)

        while left < right:
            # 计算当前面积：宽度 * 短板高度
            current_width = right - left
            current_h = min(height[left], height[right])

            # 如果当前的短板高度 * 宽度 > 历史最大，则更新
            # (这里稍微改写了一下，减少了一次乘法调用，利用 max 只比较更清晰)
            if current_width * current_h > max_area:
                max_area = current_width * current_h

            # 3. 剪枝核心：如果当前已知最大面积 >= 理论剩余最大面积，直接收工
            # 注意：这里的 current_width 是还没移动指针时的宽度
            # 实际上移动后宽度会-1，判断条件会更严苛，你的写法放在移动后判断完全没问题
            # 这里为了逻辑展示放在移动前判断也可以，只要逻辑自洽即可
            if max_area >= max_h * current_width:
                break

            # 4. 移动策略：贪心，保留长板，移动短板
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
    # 三个数之和
    # for数组每个元素，对剩余的部分双指针搜索，无序数组的指针移动判断是什么？可以先排序为升序数组
    # BigO是N2
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            # 去重逻辑 1：如果当前元素与前一个元素相同，则跳过
            # 只有当我已经处理过这个数字，再次遇到它时才跳过
            # 向前看
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    # 去重逻辑2：如果left和left-1相同，则left右移
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    # 去重逻辑2：如果right和right+1相同，则right左移
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return res
                
    # 接雨水
    # 双指针解法
    # 对于位置 i 的柱子，它能存多少水，取决于：
    # $$\text{水深} = \min(\text{左边最高的墙}, \text{右边最高的墙}) - \text{当前柱子高度}$$

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        # 1. 初始化
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        ans = 0
        
        # 2. 核心循环
        while left < right:
            # 预判：分别更新当前左右能看到的最高墙
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            # 3. 决策：哪边是短板，就处理哪边
            # 核心逻辑：如果 left_max < right_max，说明对于 left 而言，
            # 右边一定有一堵墙(即 right_max) 比 left_max 高。
            # 根据木桶效应，left 处的存水量完全由 left_max 决定。
            if left_max < right_max:
                # 谁是短板，就算谁，然后移动谁。
                # 当前这个指针位置的命运（水位），已经被那边的“短板”彻底决定了，算完就可以扔掉了，进入下一个位置。
                ans += left_max - height[left]
                left += 1
            else:
                # 同理，如果 right_max <= left_max，瓶颈在右边
                ans += right_max - height[right]
                right -= 1
                
        return ans