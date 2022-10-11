'''
给你长度相等的两个字符串 s1 和 s2 。一次 字符串交换 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。

如果对 其中一个字符串 执行 最多一次字符串交换 就可以使两个字符串相等，返回 true ；否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/check-if-one-string-swap-can-make-strings-equal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
如果不同的数多余2直接返回False
等于2就判断是否把不同的两个数交换能变成相同的
'''

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s_len = len(s1)
        num = 0
        c_s11 = c_s22 = c_s12 =c_s21 = ''
        for i in range(s_len):
            if s1[i] != s2[i] and num==0:
                c_s11 = s1[i]
                c_s21 = s2[i]
                num+=1
            elif s1[i] != s2[i] and num==1:
                c_s12 = s1[i]
                c_s22 = s2[i]
                num += 1
            elif s1[i] != s2[i]:
                num += 1
        if num>2:
            return False

        if c_s11 == c_s22 and c_s12==c_s21:
            return True
        else:
            return False



if __name__ == '__main__':
    s = Solution()
    print(s.areAlmostEqual("kleb","kleb"))
