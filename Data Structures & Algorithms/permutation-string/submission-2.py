class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        store = {}

        for c in s1:
            store[c] = store.get(c, 0) + 1

        # need = len(s1)
        storeagain={}
        for i in range(len(s1)):
            
            storeagain[s2[i]] = storeagain.get(s2[i], 0) + 1

            if storeagain==store:
                return True
        left = 0
        for right in range(len(s1),len(s2)):
            leftchar=s2[left]
            storeagain[leftchar]-=1

            if storeagain[leftchar]==0:
                del storeagain[leftchar]
            rightchar= s2[right]
            storeagain[rightchar]= storeagain.get(rightchar,0)+1

            left+=1

            if storeagain==store:
                return True
        return False



            