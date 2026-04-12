class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            s = nums[i]*nums[i]
            result.append(s)
        result.sort()
        return result
        