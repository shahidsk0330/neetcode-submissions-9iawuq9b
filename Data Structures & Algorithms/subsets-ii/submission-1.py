class Solution:
    def helper(self, i, nums, currSet, subSet):
        #base case
        if i >= len(nums):
            subSet.append(currSet[:])
            return
        
        #include
        currSet.append(nums[i])
        self.helper(i+1, nums, currSet, subSet)
        currSet.pop()

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i=i+1
        self.helper(i+1, nums, currSet, subSet) 
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        currSet, subSet =[],[]
        nums.sort()
        self.helper(0, nums, currSet, subSet)
        return subSet
        