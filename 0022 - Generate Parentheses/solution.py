# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         soln = []
#         def backtrack (string, n_open, n_close):
#             if len(string) == 2*n: 
#                 soln.append(string)
#                 return
#             if n_open < n: backtrack(string + "(", n_open + 1, n_close)
#             if n_close < n_open: backtrack(string + ")", n_open, n_close + 1)
#         backtrack("", 0, 0)
#         return soln

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i - 1 - j]:
                        dp[i].append("(" + left + ")" + right)
        
        return dp[n]
        
if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0022 - Generate Parentheses\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    ip.append(int(line.split()[-1]))
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.generateParenthesis(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass