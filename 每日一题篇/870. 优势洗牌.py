'''

给定两个大小相等的数组nums1和nums2，nums1相对于 nums2 的优势可以用满足nums1[i] > nums2[i]的索引 i的数目来描述。

返回 nums1的任意排列，使其相对于 nums2的优势最大化。

#解法（田忌赛马）：https://leetcode.cn/problems/advantage-shuffle/solution/tian-ji-sai-ma-by-endlesscheng-yxm6/

###如果田忌的下等马比齐威王的下等马好，田忌就拿下等马对齐威王的下等马，赚了，
###如果田忌下等马比不过齐威王的下等马，就用下等马比齐威王的上等马，少了一个最强对手，也是赚了

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/advantage-shuffle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        res = [0] * n
        nums1.sort()
        idx = sorted(list(range(n)),key=lambda x: nums2[x])

        left,right = 0, n-1

        for i in nums1:
            if i > nums2[idx[left]]:
                res[idx[left]] = i
                left += 1
            else:
                res[idx[right]] = i
                right -=1

        return res
if __name__ == '__main__':
    s = Solution()
    print(s.advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11]))
