class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #integer array, k
        #true: nums[i] == nums[j] # abs(i-j) <=k
        #false
        #k value  1 to size of length(array)
        for L in range(len(nums)):
            for R in range(L+1, min(len(nums), L+k+1)):
                if nums[L] == nums[R]:
                    return True
        return False


