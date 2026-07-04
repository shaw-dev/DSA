class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        store = {}

        for c in s1:
            store[c] = store.get(c, 0) + 1

        for i in range(len(s2) - len(s1) + 1):

            storeagain = {}

            for j in range(i, i + len(s1)):
                storeagain[s2[j]] = storeagain.get(s2[j], 0) + 1

            if storeagain == store:
                return True

        return False


        