class Solution:
    def findMin(self, nums: List[int]) -> int:

        
        answer= nums[0]
        for i in range(len(nums)):
            
            
            answer = min(nums[i],answer)
            
            
        return answer
        