class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        res = 0
        dic1 = {}
        row = []

        for i in range(m):
            t = sum(grid[i])
            # 每行如果大于=2就结果直接+t
            if t >= 2:
                res += t
            # 为0就不用考虑直接下一行
            elif t == 0:
                continue
            # 为1需要考虑，分别记录有哪些行和不为1的列有电脑，哪些行和为1的列有电脑
            for j in range(n):
                if grid[i][j]:

                    if t == 1:
                        if j not in dic1.keys():
                            dic1[j] = 1
                        else:
                            dic1[j] += 1
                    else:
                        row.append(j)

        for key, value in dic1.items():
            if key in row or value >= 2:
                res += value
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countServers([[0,0,0,0],[1,1,1,1],[0,0,0,1],[0,0,1,1],[0,0,0,1]]))
