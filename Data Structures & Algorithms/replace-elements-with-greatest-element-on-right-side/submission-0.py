class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_ele=-1
            for j in range(i+1,len(arr)):
                if arr[j]>max_ele:
                    max_ele =arr[j]
            arr[i] = max_ele
        arr[-1] = -1
        return arr