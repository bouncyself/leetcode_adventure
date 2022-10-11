class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        now, last = 0, 0
        num_len = len(nums)
        for i,n in enumerate(nums):
            #如果是开头
            if last == 0:
                last = n
                now += n
                if now > res:
                    res = now
            #如果不是开头
            else:
                if last < n:
                    now += n
                elif last >= n or i == num_len-1:
                    now = n
                last = n
                if now > res:
                    res = now
        return res






if __name__ == '__main__':
    s = Solution()
    print(s.maxAscendingSum([100,10,1]))