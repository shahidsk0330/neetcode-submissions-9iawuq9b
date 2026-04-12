class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output, L, R = 0, 0, len(heights)-1
        while ( L < R):
            area = min(heights[L],heights[R]) * (R-L)
            output = max(output, area)
            if(heights[L] <= heights[R]):
                L +=1
            else:
                R -=1
        return output