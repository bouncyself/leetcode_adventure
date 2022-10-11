'''
给定一个数组 prices ，它的第i个元素prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start,now_start, last,now_last = 0, 0, len(prices)-1, len(prices)-1
        start_x, last_x = prices[0], prices[last]
        res = -1
        #记录i前最小数
        minNum_beforei = [0 for i in range(len(prices))]
        #记录i后最大数
        maxNum_afteri = [0 for i in range(len(prices))]
        minNum_beforei[0] = start_x
        maxNum_afteri[last] = last_x

        for i in range(len(prices)):
            if prices[last]>=last_x :
                last_x = prices[last]
                now_last = last
                maxNum_afteri[last] = prices[last]
            else:
                maxNum_afteri[last] = maxNum_afteri[last+1]
            if prices[start] <= start_x:
                start_x = prices[start]
                now_start = start
                minNum_beforei[start] = prices[start]
            else:
                minNum_beforei[start] = minNum_beforei[start-1]

            start += 1
            last -= 1
        for i in range(len(prices)):
            res = max(res,maxNum_afteri[i] - minNum_beforei[i] )


        return res,minNum_beforei,maxNum_afteri
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([2,1,2,1,0,1,2]))