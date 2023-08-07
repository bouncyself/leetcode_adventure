'''
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[len(s)-i-1] = s[len(s)-i-1] ,s[i]
'''
题解：使用双指针，分别指向数组开头start，和结尾end
start<end时，交换s[start],s[end]，start+1，end-1
start>=end时，结束
'''


if __name__ == '__main__':
    s = Solution()
    st = ["h","e","l","l","o"]
    s.reverseString(st)
    print(st)