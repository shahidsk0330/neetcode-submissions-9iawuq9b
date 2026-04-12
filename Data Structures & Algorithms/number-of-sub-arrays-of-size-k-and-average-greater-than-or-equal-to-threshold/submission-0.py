class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sub_count = 0
        for L in range(len(arr)-k+1):
            sub_sum= arr[L]
            for R in range(L+1, L+k):#0
                sub_sum += arr[R]
            if sub_sum//k >= threshold:
                sub_count +=1
        return sub_count


        
        