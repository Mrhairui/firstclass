class Solution:
    def twoSum(self, nums, target):
        _dict = {}
        for i, m in enumerate(nums):
            if _dict.get(target - m) is not None:           # 从前面一直往里加字典，首先第一个值进去，当到第二个值的时候，就会停下，因为第一个值已经进去了
                return[i, _dict.get(target - m)]
            _dict[m] = i

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 18))