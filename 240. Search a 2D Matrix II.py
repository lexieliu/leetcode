class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        '''
        row = len(matrix)
        col = len(matrix[0])
        j = col - 1
        i = 0
        while True:
            while j>=0 and target < matrix[i][j]:
                j -= 1
            if j == -1:
                return False
            if target == matrix[i][j]:
                return True
            i += 1
            if i == row:
                return False
        '''
        
        
        
        
        row = len(matrix)
        col = len(matrix[0])
        j = col -1
        for i in range(row):
            while j>= 0 and target < matrix[i][j]:
                j -= 1
            if j == -1:
                return False
            if target == matrix[i][j]:
                return True
            
        return False
