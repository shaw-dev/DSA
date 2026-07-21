class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left =0
        right = len(heights)-1
        maxarea=0
        while left<right:
            
            minimum=min(heights[left],heights[right])
            width = right-left
            answer = minimum*width
            maxarea=max(maxarea, answer)
            if heights[left] <heights[right]:
            
                left+=1
            else:
                right-=1
        
            

        return maxarea

        