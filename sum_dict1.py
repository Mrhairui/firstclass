class Solution:
    def twoSum(self, nums, target) :
        _dict = {}
        for i, m in enumerate(nums):
            _dict[m] = i
        for i, m in enumerate(nums):    # 生成序号和值得对应
            j = _dict.get(target - m)  # 字典中要查找的key
            if j is not None and j != i:
                return[i, j]

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 18))