class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #k=1 #k is range is between 1 and max value of piles:
        L,R = 1, max(piles)
        outcome = R
        while(L <= R):
            m = L + (R - L)//2
            total_hours = 0
            for pile in piles:
                pile_hours = (pile + m -1)//m
                total_hours += pile_hours
            if(total_hours <= h):
                outcome = m
                R = m -1
            elif(total_hours >h):
                L = m + 1
        return outcome

