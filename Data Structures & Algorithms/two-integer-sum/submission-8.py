class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in num:
                return [num[t], i]
            else:
                num[nums[i]] = i
        