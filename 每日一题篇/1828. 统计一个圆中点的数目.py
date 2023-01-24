class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        for q in queries:
            num = 0
            for p in points:
                d = (p[0]-q[0])**2+(p[1]-q[1])**2
                if d <= q[2]**2:
                    num += 1
            answer.append(num)
        return answer

if __name__ == '__main__':
    s = Solution()
    print(s.countPoints(points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]))