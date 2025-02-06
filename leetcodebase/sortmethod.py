"""
author:guoxu
date:2025-02-06
introduction:这个代码记录常见的基础排序方法，注意每个方法的特点，时间复杂度和数据相对性
"""
# 选择排序：每次在剩下的序列中选择最小的数
# 时间复杂度：O(N^2)
# 算法特点：从头有序，强制性比较，O(N^2)
def seletction_sort(nums):
    for i in range(len(nums)):
        # 找到剩余序列中最小元素的序列
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        # 交换
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

# 冒泡排序：剩下的序列中每次一个数滚到最后
# 时间复杂度：O(N^2)
# 算法特点：从尾有序，部分有序会早停
def bubble_sort(nums):
    n = len(nums)
    # 循环n次，每次确定一个数
    for i in range(n):
        # 标记是否有数据交换
        swap_tag = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap_tag = True
        # 如果当前轮次没有数据交换，说明目前的序列已经有序
        if not swap_tag:
            break
    return nums

# 插入排序：打牌时整理牌，有序的手牌和发的新牌，左小右大
# 时间复杂度：O(N^2)
# 算法特点：依赖初始排序顺序，适合部分有序的序列，完全有序则O(N)，逆序则O(N^2)
def insertion_sort(nums):
    for i in range(1, len(nums)):
            # key是待插入的数据
            key = nums[i]
            j = i - 1
            # j找到小于等于key的位置
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
    return nums

# 归并排序：分治法的思想，将序列递归地分成两组，分别排序后再合并
# 时间复杂度：O(nlogn)，每次合并的时间是O(n)，数组二分形成一个二叉树，合并次数与分叉有关
# 空间复杂度：O(n)
# 算法特点：递归的思想，二叉树的后序遍历
def merge_sort(nums):
    # 递归思想，经过函数的处理子序列已经有序
    # 边界条件
    if len(nums) > 1:
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        # 左右子序列已经有有序
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1
    return nums

# 快速排序：分治法思想，选择一个枢纽元素，将数组分为两部分，左小右大，递归地对两部分排序
# 时间复杂度：平均O(nlogn)，最坏O(n^2)，最好O(nlogn)
# 空间复杂度：原地快排，不占用额外空间
# 算法特点：
def quick_sort(nums, low, high):
    # 边界条件
    if low < high:
        # 找到序列中的基准元素, 
        # 将数组重新排列，使得所有小于基准的元素位于基准左侧，所有大于基准的元素位于右侧。
        # 分区完成后，基准元素位于其最终位置。
        pi = partition(nums, low, high)

        # 递归对左右序列排序
        quick_sort(nums, low, pi-1)
        quick_sort(nums, pi+1, high)
    

def partition(arr, low, high):
    # 选择基准元素（这里选择最后一个元素）
    pivot = arr[high]
    i = low - 1  # 指向小于基准的最后一个元素
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素
    
    # 将基准元素放到正确位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# 简单思路
# 时间复杂度：平均O(nlogn)，最坏O(n^2)，最好O(nlogn)
# 空间复杂度：
def quick_sort_simple(arr):
    # 定义这个函数实现的功能：
    # 1找到基准元素并确定位置；
    # 2将数组重新排列，使得所有小于基准的元素位于基准左侧，所有大于基准的元素位于右侧；
    
    # 边界条件：如果数组长度小于等于1，直接返回（递归终止条件）
    if len(arr) <= 1:
        return arr
    
    # 选择基准元素（这里选择最后一个元素）
    pivot = arr[-1]
    
    # 初始化左右分区
    left = [x for x in arr[:-1] if x <= pivot]  # 小于等于基准的元素
    right = [x for x in arr[:-1] if x > pivot]  # 大于基准的元素
    
    # 递归排序左右分区，并合并结果
    return quick_sort_simple(left) + [pivot] + quick_sort_simple(right)

def test_sort():
    pass