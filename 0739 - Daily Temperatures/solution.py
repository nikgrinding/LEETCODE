# class Solution(object):
#     def dailyTemperatures(self, temperatures):
#         """
#         :type temperatures: List[int]
#         :rtype: List[int]
#         """
#         answer = [0]*len(temperatures)
#         stack = []
#         for i in range(len(temperatures)):
#             while stack and temperatures[i] > temperatures[stack[-1]]:
#                 top = stack.pop()
#                 answer[top] = i - top
#             stack.append(i)
#         return answer

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0]*len(temperatures)
        hottest_temp = 0
        for i in range(len(temperatures)-1, -1, -1):
            if temperatures[i] > hottest_temp:
                hottest_temp = temperatures[i]
                continue
            days = 1
            while temperatures[i] >= temperatures[i+days]:
                days += answer[i+days]
            answer[i] = days
        return answer      
        

if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0739 - Daily Temperatures\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str = line.split()[-1][1:-1]
                    l_list = [int(i) for i in l_str.split(",")]
                    ip.append(l_list)
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.dailyTemperatures(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass