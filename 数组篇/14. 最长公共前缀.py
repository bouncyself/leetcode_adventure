class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        index = 0
        res = ""
        i_len = min(len(s) for s in strs)

        for i in range(i_len):
            temp = strs[0][i]
            for s in strs:
                if s[i] != temp:
                    return res
            res += temp



        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))