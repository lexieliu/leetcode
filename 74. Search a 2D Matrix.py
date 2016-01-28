class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 1:
            return target in matrix[0]
        row = len(matrix)
        col = len(matrix[0])
        up = 0 
        down = row-1
        while up <= down:
            mid = (up+down)/2
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                return target in matrix[mid]
            elif  target < matrix[mid][0]:
                down = mid-1
            else:
                up = mid+1
        return False
            
