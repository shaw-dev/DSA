class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]* n

        pref = 1
        for i in range(n):
            res[i]=pref #still 1
            pref*=nums[i]
            print(pref)
        
        suff =1
        for i in range(n-1,-1,-1):
            res[i] *= suff #still1
            suff*=nums[i]
            print(suff)

        return res


        

