class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key={}

        for i in range(len(nums)):
            if nums[i] in key:
                return [key[nums[i]],i]
            diff = target-nums[i]
            if nums[i] not in key:
                key[diff] =i
        
        

        