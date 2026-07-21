class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        count ={}

        for i in nums:
            count[i] = 1+count.get(i,0)

        new =[]
        for i, j in count.items():
           new.append([j,i])
        new.sort()

        ans = []
        while len(ans)<k:
            ans.append(new.pop()[1])
        return ans
