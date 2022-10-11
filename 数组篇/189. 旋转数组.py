'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数
'''

class Solution():
    def spinList1(self,num,k):
        res = num[-k:]
        res.extend(num[0:-k])
        return res
    #先反转整个数组，再反转前k个，再反转后len-k个
    def spinList2(self, num, k):
        temp = num[::-1]
        res1 = temp[:k]
        res2 = temp[k:][::-1]
        res1.extend(res2)
        return res1

if __name__ == '__main__':
    s = Solution()
    # print(s.spinList1([1,2,3,4,5,6,7,8],3))
    print(s.spinList2([1,2,3,4,5,6,7,8],4))