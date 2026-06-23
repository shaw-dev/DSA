class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        for i in range(len(nums)):
            if nums[i] != target:
                i+=1
            elif nums[i] == target:
                return i
        return -1