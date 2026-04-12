class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0,len(nums)-1
        while(L <= R):
            mid = L + (R-L)//2
            #case-1: number may fall into Left  sub array
            #case-2: number may fall into right right array
            #case-3: mid element is the target
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                R = mid -1
            elif(nums[mid] < target):
                L = mid + 1
        return -1
        