class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = []
        dict = {}

        #遍历cpdomains取出所有子域
        for c in cpdomains:
            temp = c.split(' ')
            num = int(temp[0])
            s = temp[1].split('.')
            t = ''
            for i in range(len(s)):
                t = s[len(s)-1-i] + '.' + t
                if i==0:
                    t = t[:-1]
                if t not in dict.keys():
                    dict[t] = num
                else:
                    dict[t] += num
        for key,val in dict.items():
            res.append(str(val)+" "+key)

        return res