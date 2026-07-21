class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={}
        maxlen= 0
        length= len(s)
        left=0

        for right in range(length):
            current = s[right]

            counts[current]= counts.get(current,0)+1
            maxfreq= max(counts.values()) #counting what we have
            windowlen = right-left+1


            while windowlen-maxfreq>k:
                leftchar= s[left]
                counts[leftchar]-=1
                left+=1
                maxfreq= max(counts.values())
                windowlen=right-left+1
            maxlen = max(maxlen, windowlen)
        return maxlen

