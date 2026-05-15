class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0 , len(heights)-1
        maximum_water = 0
        while left< right: 
            minimum_bar = min(heights[left], heights[right])
            distance = right - left
            amount = minimum_bar * distance
            if heights[left] <= heights[right]:
                left +=1
            else:
                right -=1
            maximum_water = max(amount, maximum_water)
            
        return maximum_water

        