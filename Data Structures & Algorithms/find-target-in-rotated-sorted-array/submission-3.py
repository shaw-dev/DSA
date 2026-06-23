class Solution:

    def search(self, nums: List[int], target: int) -> int:

        l =0
        r = len(nums)-1
        while l<=r:
            middle = l+(r-l)//2
            if nums[middle] == target:
                return middle
            if nums[l] <= nums[middle]: #left half is sorted
                
                if nums[l] <= target<nums[middle]:
                    r= middle-1
                else:
                    l = middle +1
            else:
                #right half sorted:
                if nums[middle] < target<=nums[r]:
                    l = middle +1
                else:
                    r = middle-1
           
        return -1

        