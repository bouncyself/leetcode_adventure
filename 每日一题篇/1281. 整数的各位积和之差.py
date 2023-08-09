'''
给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
'''
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s_n = str(n)
        res1 = 1
        res2 = 0
        for i in s_n:
            res1 = res1 * int(i)
            res2 = res2 + int(i)
        return res1 - res2



if __name__ == '__main__':
    s = Solution()
    n= 4421
    print(s.subtractProductAndSum(n))
