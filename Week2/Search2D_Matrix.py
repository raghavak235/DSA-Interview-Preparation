https://leetcode.com/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=top-interview-150

# Time Complexity: O(m*n)
# Space Complexity: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # m -> number of rows
        # n-> number of columns 
        m = len(matrix)
        n = len(matrix[0])
        
        low, high = 0, m*n -1
        
        while low <= high:
            mid  = low + (high - low)//2

            # formula for to get mid indexes(n is number orf cols 4)
            row_idx = mid//n
            col_idx = mid%n
            midelement = matrix[row_idx][col_idx]
            
            if midelement == target:
                return True
            
            # 3 < 16
            # move the index to left
            
            elif target < midelement:
                high = mid-1
            
             # move the index to right
            else:
                low = mid +1

        return False



