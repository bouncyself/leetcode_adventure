class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        dic1 = {}
        for l in logs:
            if l[0] not in dic1.keys():
                dic1[l[0]] = {l[1]}
            else:
                dic1[l[0]].add(l[1])
        answer = [0]*k
        for key in dic1:
            answer[len(dic1[key])-1] += 1
        return answer

if __name__ == '__main__':
    s = Solution()
    print(s.findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5))
