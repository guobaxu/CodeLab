# 两数之和
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
def twosum(nums:list[int], target:int) -> list[int]:
    res_idx = [0,0]
    for i in range(len(nums)):
        if (target - nums[i]) in nums:
            res_idx[0] = i
            for j in range(i+1, len(nums)):
                if nums[j] == (target - nums[i]):
                    res_idx[1] = j
                    return res_idx
# 上面的方法本质还是多个for嵌套，in操作的时间复杂度取决于被查询的数据结构：
# O(n)：list，str，tuple
# O(1)：set，dict

def twosum_hash(nums:list[int], target:int) -> list[int]:
    hashtb = dict() # 键值对：nums[i] --> i
    for i, num in enumerate(nums):
        if target - num in hashtb:
            return [hashtb[target - num], i]
        hashtb[num] = i
    return []