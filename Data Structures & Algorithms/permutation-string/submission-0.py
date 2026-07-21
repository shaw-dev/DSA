class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)> len(s2):
            return False
        
        storevals={} #trying to store values here
        for i in s1:
            
            storevals[i] = storevals.get(i,0)+1
            # i+=1
        windowsize=len(s1)
        windowcount={}
        for right in range(len(s2)):
            righthing = s2[right]
            windowcount[righthing] = windowcount.get(righthing,0)+1

            if right>= windowsize:
                left = s2[right-windowsize]
                windowcount[left]-=1

                if windowcount[left]==0:
                    del windowcount[left]
            
            if windowcount==storevals:
                return True
            
            
        return False
        



        