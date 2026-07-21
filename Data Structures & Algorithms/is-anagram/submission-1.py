class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        d = sorted(s)
        f = sorted(t)
        if len(d)!= len(f):
            return False
        for i in range(len(d)):
            if d[i]!=f[i]:
                return False
        return True
            