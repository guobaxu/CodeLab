
# 滑动窗口模板
import string

'''
def sliding_window(nums):
    # 1. 初始化
    left = 0
    right = 0
    window_data = {} # 或 set() / int(sum)，视题目而定
    ans = ...        # 初始化结果 (求最小设为 inf, 求最大设为 0)

    # 2. 核心循环：主动右移 (Expand)
    for right in range(len(nums)):
        # 1. 获取即将进窗口的字符/数字
        c = nums[right] # 即将移入窗口的字符/数字
        
        # --- A. 进窗口 (In) ---
        # 更新窗口数据，例如：window_data[c] += 1 或 current_sum += c
        
        # --- B. 什么时候收缩？ (Shrink Condition) ---
        # CASE 1: 求最短/最小类 (例如：长度最小的子数组) -> 满足条件时收缩
        # while window_valid(window_data):
        
        # CASE 2: 求最长/最大类 (例如：最长无重复子串) -> 不满足条件时收缩 (使其变合法)
        # while not window_valid(window_data):
            
            d = nums[left] # 即将移出窗口的字符/数字
            
            # --- C. 出窗口 (Out) ---
            # 更新窗口数据，例如：window_data[d] -= 1 或 current_sum -= d
            
            left += 1 # 左指针右移，窗口缩小
            
            # --- D. 更新答案 (Update Answer) ---
            # 注意：更新答案的位置取决于题目是求“长”还是“短”
            # 求最短：通常在 while 循环内部，收缩之前或之后更新
            # 求最长：通常在 while 循环结束后更新 (此时窗口一定合法)
        
    return ans
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window_data = [] # 字典检索的话会比较快
        ans = 0

        def window_valid(window_data):
            # 判断window_data是否有重复元素 有重复返回False，没有重复返回True
            return len(window_data) == len(set(window_data))
        
        # for循环是一次进一个字符，然后判断是否收缩
        for right in range(len(s)):
            c = s[right]
            # 进窗口
            window_data.append(c)
            
            # 判断是否收缩
            while not window_valid(window_data):
                d = window_data.pop(0)
                left += 1
            
            # 更新答案
            ans = max(ans, right - left + 1)
            
        return ans

    # 时间优化
    def lengthOfLongestSubstring_set(self, s: str) -> int:
        left = 0
        # 优化点 1: 使用 set 而不是 list
        # lookup 时间从 O(N) 降为 O(1)
        window_set = set() 
        ans = 0

        for right in range(len(s)):
            # 1.获取即将进窗口的字符
            c = s[right]
            
            # 优化点 2: 判断是否收缩
            # 这里的逻辑是：如果即将进来的 c 已经在窗口里了，那就是重复了
            # 我们需要一直缩，直到把那个重复的字符“挤出去”为止
            # 2.进窗口前判断（可能需要收缩）
            while c in window_set:
                # 出窗口：移除最左边的元素
                # 我们不需要 list.pop(0)，因为 s[left] 就是最左边的元素
                window_set.remove(s[left])
                left += 1
            
            # 3.进窗口
            # 这一步必须放在 while 之后，确保窗口里没有 c 了，再把它加进来
            window_set.add(c)
            
            # 4.更新答案
            ans = max(ans, right - left + 1)
            
        return ans

    # 跳跃式收缩
    def lengthOfLongestSubstring_dic(self, s: str) -> int:
        # 记录每个字符最后出现的位置 {char: index}
        dic = {}
        left = 0
        ans = 0
        
        # 1.获取即将进窗口的字符和index
        for right, c in enumerate(s):

            # 如果 c 在字典里，且在当前窗口内（即 index >= left）
            # 2.进窗口前判断是否收缩
            if c in dic and dic[c] >= left:
                # 直接跳到重复字符的下一位
                left = dic[c] + 1
            
            # 3.更新/记录字符的最新位置
            dic[c] = right
            # 4.更新答案
            ans = max(ans, right - left + 1)
            
        return ans
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 0. 边界防守
        if len(s) < len(p):
            return []

        # 固定窗口长度
        window_len = len(p)
        left = 0
        ans = []
        
        # 1. 初始化字典
        # 建议：直接用 Counter 或者手动构建 p_dict
        from collections import Counter
        p_dict = Counter(p) 
        window_dict = {}

        # 预填窗口：先把前 k-1 个填进去 (这样进入主循环时可以直接 "进1-判1-出1")
        for i in range(window_len - 1):
            char = s[i]
            window_dict[char] = window_dict.get(char, 0) + 1

        # 2. 主循环
        for right in range(window_len - 1, len(s)):
            # --- A. 进窗口 ---
            c = s[right]
            window_dict[c] = window_dict.get(c, 0) + 1
            
            # --- B. 判断是否符合标准 ---
            # Python 字典可以直接用 == 比较，它会比较 Key 和 Value 是否完全一致
            # 这比你自己写的 judge_func 快且安全
            if window_dict == p_dict:
                ans.append(left)
            
            # --- C. 出窗口 ---
            remove_c = s[left]
            window_dict[remove_c] -= 1
            
            # 🔥 关键修正：如果减到 0，必须删除 Key！
            # 否则 {'a': 0} != {}，会导致后续比较出错
            if window_dict[remove_c] == 0:
                del window_dict[remove_c]
            
            left += 1
            
        return ans

"""
Counter 是 Python 标准库 collections 里的一个类。
from collections import Counter
s = "banana"
count = Counter(s)
# 结果: Counter({'a': 3, 'n': 2, 'b': 1})

普通的字典访问不存在的 Key 会报错 KeyError。 Counter 访问不存在的 Key，会返回 0。
c = Counter("abc")
print(c['z']) # 输出 0，不会报错！
"""