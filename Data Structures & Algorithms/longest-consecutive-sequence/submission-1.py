class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        if len(nums) ==0:
            return 0
        longest =1 

        for num in new:
            if num -1 not in new:
                current = num
                length =1

                while current+1 in new:
                    current = current+1
                    length+=1
                longest = max(longest,length)
        return longest

