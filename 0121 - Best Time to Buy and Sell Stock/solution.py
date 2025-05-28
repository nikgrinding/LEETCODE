# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """

#         profit = 0

#         l_ptr, r_ptr = 0, 1
#         while r_ptr < len(prices):
#             if prices[l_ptr] < prices[r_ptr]:
#                 profit = max(profit, prices[r_ptr] - prices[l_ptr])
#             else:
#                 l_ptr = r_ptr
#             r_ptr += 1
        
#         return profit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        min_stock = prices[0]

        for stock in prices:
            min_stock = min(min_stock, stock)
            profit = max(profit, stock - min_stock)
        
        return profit
        
        
if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0121 - Best Time to Buy and Sell Stock\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str = line.split()[-1]
                    l_list = [int(i) for i in l_str[1:-1].split(",")]
                    ip.append(l_list)
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.maxProfit(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass