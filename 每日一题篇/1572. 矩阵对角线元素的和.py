'''
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
'''
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        res = 0
        for i in range(n):
            for j in range(n):
                if (i+j) == (n-1):
                    res+=mat[i][j]
        if n%2==0:
            for i in range(n):
                res += mat[i][i]
        else:
            for i in range(n):
                if i != (n/2):
                    res+=mat[i][i]
        return res

if __name__ == '__main__':
    s = Solution()
    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    print(s.diagonalSum(mat))