class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            j,k = i+1, len(nums)-1
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s ==0:
                    tmp = [nums[i],nums[j],nums[k]]
                    res.add(tuple(tmp))
                    j+=1
                    k-=1
                elif s>0:
                    k-=1
                else:
                    j+=1
        return [list(ele) for ele in res]
        