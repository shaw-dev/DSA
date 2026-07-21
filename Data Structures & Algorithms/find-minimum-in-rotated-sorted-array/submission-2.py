class Solution:
    def findMin(self, nums: List[int]) -> int:

        #lets keep the same pointers for l and r

        l =0
        r = len(nums)-1
        
        for i in range(len(nums)):
            pointer = l+(r-l)//2
            middle = nums[pointer]
            
            if middle>nums[r]:
                l= pointer+1
            else:
                r= pointer
        
        return nums[l]
            
        