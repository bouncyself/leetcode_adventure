'''
给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。

如果可以将 x恰好 减到0 ，返回 最小操作数 ；否则，返回 -1 。
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        step = 0
        def digui(nums, x, step):
            if x < 0:
                return
            if x == 0:
                return step
            digui(nums[1:],x-nums[0], step+1)
            digui(nums[:-1],x-nums[len(nums)-1],step+1)
        return digui(nums, x, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations([1,1,4,2,3],5))
    print(s.minOperations([5,6,7,8,9],4))
    print(s.minOperations([3,2,20,1,1,3],10))
