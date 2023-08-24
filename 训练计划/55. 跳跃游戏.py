class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #长度为1
        if len(nums) == 1:
            return True
        res = [0]*len(nums)
        #长度为2
        index = len(nums)-2
        if index == 0:
            if nums[0] >=1:
                return True
            else:
                return False
        res[-1] = 1

        #长度大于2
        while index!=-1:
            len1 = index+nums[index] if (index+nums[index])<=(len(nums)) else len(nums)

            if sum(res[index+1:len1+1]) >0:
                res[index] = 1
            index -= 1
        if res[0]:
            return True
        else:
            return False
'''
题解：
记录每个点最多能跳到哪，遍历所有的点，如果最后能跳到的最远点k，比i小，就代表他没有跳到最后一格，如果k比i大，就代表能跳到最后一格
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int k = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i > k) return false;
            k = max(k, i + nums[i]);
        }
        return true;
    }
};

作者：Ikaruga
链接：https://leetcode.cn/problems/jump-game/solutions/24322/55-by-ikaruga/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

if __name__ == '__main__':
    s = Solution()
    print(s.canJump(nums = [2,3,1,1,4]))
