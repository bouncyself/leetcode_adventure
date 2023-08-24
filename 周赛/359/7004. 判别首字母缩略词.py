class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        res = ""
        for i in words:
            res+=i[0]
        if res == s:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isAcronym())