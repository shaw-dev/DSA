class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        seen=set()
        maxl=0
        left =0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            curent = right-left+1
            maxl=max(maxl,curent)
        return maxl