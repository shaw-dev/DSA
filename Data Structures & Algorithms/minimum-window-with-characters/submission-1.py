class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        need={}
        formed=0
        res=[-1,-1]
        length=float('inf')

        for c in t:
            need[c]= need.get(c,0)+1
        #now i have all the c in t
        window={}

        left=0
        for right in range(len(s)):
            c= s[right]
            window[c]=window.get(c,0)+1
            

            if c in need and window[c]==need[c]:
                formed+=1
            while len(need)==formed:
                if right-left+1<length:
                    length = right-left+1
                    res = [left,right]

                leftchar= s[left]
                window[leftchar]-=1
                if leftchar in need and window[leftchar]<need[leftchar]:
                    formed-=1
                left+=1
        if length==float('inf'):
            return ""
        return s[res[0]:res[1] + 1]
            
            
                

            


        