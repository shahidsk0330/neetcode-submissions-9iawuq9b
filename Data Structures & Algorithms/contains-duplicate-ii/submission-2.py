class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L=0
        for right in range(len(nums)):
            if len(window) > k:
                window.remove(nums[L])
                L+=1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False
        
        