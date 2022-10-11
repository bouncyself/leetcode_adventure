class Solution(object):
    # def intersect(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: List[int]
    #     """
    #     #遍历一遍nums1, 创建映射
    #     dict = {}
    #     res = []
    #     for n in nums1:
    #         if n not in dict.keys():
    #             dict[n] = 1
    #         else:
    #             dict[n] += 1
    #     for n in nums2:
    #         if n in dict.keys() and dict[n]!=0:
    #             res.append(n)
    #             dict[n] -= 1
    #     return res

    #进阶版，如果是有序的
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        index1,index2 = 0,0
        len_n1,len_n2 = len(nums1),len(nums2)

        while index1<len_n1 and index2<len_n2:
            if nums1[index1] == nums2[index2]:
                res.append(nums1[index1])
                index1 += 1
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1


        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intersect([4,9,5],[9,4,9,8,4]))

