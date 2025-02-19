"""
author:guoxu
date:2025-02-18
introduction:在有序数组中的二分查找目标值
"""
class Solution:
    def search(self, nums:list[int], traget:int)->int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == traget:
                return mid
            elif nums[mid] < traget:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

# 二分查找升级版
# 找到target最后一次出现的下标
# 如：在[1,2,4,4,5,7]中找4，返回index=3
class Solution:
    def search(self, nums:list[int], traget:int)->int:
        left, right = 0, len(nums)-1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == traget:
                result = mid
                left = mid + 1
            elif nums[mid] < traget:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
