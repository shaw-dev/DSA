import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l =1
        r =max(piles)
        answer = r

        while l<=r:
            middle = l + (r-l)//2
            hours =0
            for i in piles:
                hours+= math.ceil(i/middle)

            if hours > h:
                l = middle+1
            elif hours<=h:
                answer =k=middle
                r= middle -1
        return answer 



            
        