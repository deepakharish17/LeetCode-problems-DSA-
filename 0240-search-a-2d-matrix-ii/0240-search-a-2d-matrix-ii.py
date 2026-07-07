class Solution(object):
    def searchMatrix(self, matrix, target):
        # n = len(matrix)
        # m = len(matrix[0])
        # low = 0
        # high = n * m - 1
        # while low<=high:
        #     mid=(low + high)// 2
        #     row = mid // m
        #     col = mid % m
        #     if matrix[row][col]==target:
        #         return True
        #     elif target>matrix[row][col]:
        #         low=mid+1
        #     else:
        #         high=mid-1
        # return False
       
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==target:
                    return True
        return False