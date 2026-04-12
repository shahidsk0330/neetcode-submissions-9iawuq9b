class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #integer array, k
        #true: nums[i] == nums[j] # abs(i-j) <=k
        #false
        #k value  1 to size of length(array)
        window = set()
        L = 0 
        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False


