class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l =0
        r = len(matrix) * len(matrix[0])-1
        while l<=r:
            mid = l+(r-l)//2
            row = mid//len(matrix[0])
            column = mid%len(matrix[0])
            if matrix[row][column]<target:
                l=mid+1
            if matrix[row][column]>target:
                r = mid-1
            elif matrix[row][column]== target:
                return True     
        return False   