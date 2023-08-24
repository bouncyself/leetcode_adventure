class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_n(num):
            res = -1
            while num:
                t = num%10
                if t>res:
                    res = t
                num = num//10
            return res

        dic = {}
        for i,num in enumerate(nums):
            n = get_n(num)
            if n not in dic.keys():
                dic[n] = [num]
            else:
                dic[n].append(num)
        res = -1
        for key,value in dic.items():
            if len(value)>=2:
                dic[key] = sorted(dic[key],reverse=True)
                if (dic[key][0]+dic[key][1])>res:
                    res = dic[key][0]+dic[key][1]
        return res




if __name__ == '__main__':
    s = Solution()
    print(s.maxSum([51,71,17,24,42]))
