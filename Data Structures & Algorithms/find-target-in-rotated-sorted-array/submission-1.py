class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #rotated array: Two sorted arrays
        #find the pivot element index: (smallest element in the array) using bs
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right- left)//2
            if (nums[mid] > nums[right]):
                left = mid +1
            else: 
                right = mid
        pivot = left

        def binarysearch(left,right):
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return mid
                elif(nums[mid] > target):
                    right = mid -1
                else:
                    left = mid + 1
            return -1
        result = binarysearch(0,pivot-1)
        if result != -1:
            return result

        return binarysearch(pivot, len(nums)-1)
        
        