class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R = 0 ,len(numbers)-1
        while (L < R):
            sum_pair = numbers[L] + numbers[R]
            #isEqual
            if(sum_pair == target):
                return [L+1, R+1]
            #isGreater
            elif(sum_pair > target):
                R-=1
            #isSmaller
            elif(sum_pair < target):
                L+=1
        

        

        


        