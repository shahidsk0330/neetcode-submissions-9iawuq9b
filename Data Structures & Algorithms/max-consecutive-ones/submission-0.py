class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        """
        The problem statement tells that we have a binary array nums (0 or 1s) we have to return the maximum number of consecutive(next to each other). if no 1's are present then resutlt is 0 if 1's present and minum consecuitive value is 1 and max will be the length of the array. 
    if data point is 1 then need to check next data points until it reaches to end of the list or we found 0. to caluculate the current consecutive sub part we will store in the variable curr_consecutive initialy as 1 because we initializy when the data point is 1. 
    I will use here two for loops one loop to travel from 0 to n. other loop is to calculate the lenght of the consecutive number sub array. 
        """
        max_consecutive=0
        for i in range( len(nums)):
            if nums[i]==1: 
                curr_consecutive = 1
                j=i+1
                while(j< len(nums) and nums[j]!=0):
                    curr_consecutive +=1
                    j+=1
                max_consecutive = max(curr_consecutive, max_consecutive)
        return max_consecutive
                    