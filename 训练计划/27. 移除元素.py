class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        index = len(nums) - 1
        res = 0
        for n in nums:
            if n !=val:
                res+=1
        if res == 0:
            nums=[]
            return res
        elif res == len(nums):
            return res

        index = len(nums)-1
        for i in range(res):
            if nums[i] == val:
                while nums[i] == val and index!=0:
                    nums[i],nums[index] = nums[index],nums[i]
                    index -= 1


        return res,nums
'''
题解：用双指针，一个指向left,一个指向right
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left = 0, right = nums.size();
        while (left < right) {
            if (nums[left] == val) {
                nums[left] = nums[right - 1];
                right--;
            } else {
                left++;
            }
        }
        return left;
    }
};

'''
if __name__ == '__main__':
    s = Solution()
    print(s.removeElement(nums = [3,3], val = 3))