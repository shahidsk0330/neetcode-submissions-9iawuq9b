class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for index in range(len(nums)):
            look_up_value = target-nums[index]
            if look_up_value in numsMap:
                return [numsMap[look_up_value],index]
            else:
                numsMap[nums[index]] = index
  
        
        
        

        