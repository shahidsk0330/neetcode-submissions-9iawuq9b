# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output =[]
        for sub in range(len(pairs)):
            L= sub-1
            while(L>=0 and pairs[L].key> pairs[L+1].key ):
                pairs[L],pairs[L+1] = pairs[L+1],pairs[L]
                L=L-1
            output.append(pairs[:])
        return output
        

        