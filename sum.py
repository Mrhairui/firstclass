class Solution:
    def twoSum(self, nums, target) :
        nums = sorted(nums)
        i=0
        j=0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 18))