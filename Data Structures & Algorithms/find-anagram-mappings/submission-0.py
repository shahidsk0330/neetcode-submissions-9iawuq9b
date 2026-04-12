class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_dct ={}
        result =[]
        for i in range(len(nums2)):
            nums2_dct[nums2[i]] = i
        for nums in nums1:
            result.append(nums2_dct[nums])
        return result
