'''

#把()看作(0)的情况
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]
        for c in s:
            if c == '(':
                st.append(0)
            else:
                v = st.pop()
                st[-1] += max(2 * v, 1)
        return st[-1]

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/score-of-parentheses/solution/gua-hao-de-fen-shu-by-leetcode-solution-we6b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re

        while '(' in s or ')' in s:
            s = s.replace("()", "1")
            lst = re.findall("\([1-9]\d*\)", s)
            for l in lst:
                s= s.replace(l, '1'*(len(l)-2)*2)


        return len(s)







if __name__ == '__main__':
    s = Solution()
    print(s.scoreOfParentheses("(()(()))"))


