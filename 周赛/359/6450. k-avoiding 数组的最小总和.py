class Solution(object):
    def maximizeTheProfit(self, n, offers):
        """
        :type n: int
        :type offers: List[List[int]]
        :rtype: int
        """
        sums = [0]*len(offers)
        res = -1
        while sum(sums) != len(offers):
            e = -1
            r = 0
            for i,offer in enumerate(offers):

                if 1 in sums[offer[0]:offer[1]]:
                    continue
                else:
                    if offer[0] > e:
                        e = offer[1]
                        r += offer[2]

                        sums[offer[0]:offer[1]] = [1] * len(sums[offer[0]:offer[1]])
                        if r>res:
                            res = r
        return res




if __name__ == '__main__':
    s = Solution()
    print(s.maximizeTheProfit(n = 4, offers = [[0,0,5],[3,3,1],[1,2,5],[0,0,7]]))
