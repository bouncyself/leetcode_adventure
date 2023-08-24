class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        s = start.replace("_","")
        t = target.replace("_","")
        if s == t:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.canChange("_R", target = "R_"))
