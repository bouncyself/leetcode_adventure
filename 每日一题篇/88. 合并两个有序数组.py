class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        t1 = m
        t2 = n
        t3 = n+m

        while t1>0 and t2>0:
            n1 = nums1[t1-1]
            n2 = nums2[t2-1]
            if n1 > n2:
                nums1[t3-1] = n1
                t1 -= 1
            else:
                nums1[t3 - 1] = n2
                t2 -= 1
            t3 -= 1
        if t2 > 0:
            for i in range(t2):
                nums1[i] = nums2[i]




if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(s.merge(nums1,m,nums2,n))

