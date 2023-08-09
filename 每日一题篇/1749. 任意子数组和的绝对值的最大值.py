'''
给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 和的绝对值 为 abs(numsl + numsl+1 + ... + numsr-1 + numsr) 。

请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。

abs(x) 定义如下：

如果 x 是负整数，那么 abs(x) = -x 。
如果 x 是非负整数，那么 abs(x) = x 。
'''
class Solution(object):
    def maxAbsoluteSum(self, nums):
        res = 0
        res_max = -1
        for n in nums:
            if (res+n)>=0:
                res+=n
                if res>res_max:
                    res_max = res
            else:
                res = 0
        nums = [-i for i in nums]
        res = 0
        res_max2 = -1
        for n in nums:
            if (res+n)>=0:
                res+=n
                if res>res_max2:
                    res_max2 = res
            else:
                res = 0

        return max(res_max,res_max2)

'''
题解：
最大前缀和-最小前缀和即为最大子数组
nums = [1,-3,2,3,-4]
max_list = [1,-3,2,3]  max_sum = 3
min_list = [1,-3]  min_sum = -2
max_sum-min_sum = 5
'''

if __name__ == '__main__':
    s = Solution()
    nums = [1,-3,2,3,-4]
    print(s.maxAbsoluteSum(nums))
