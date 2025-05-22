class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        answer = 0
        stack = []

        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[i] < heights[stack[-1]]):
                h = heights[stack.pop()]
                w = i if not stack else i - (stack[-1]+1)
                answer = max(answer, h*w)
            stack.append(i)
        return answer
        
if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0084 - Largest Rectangle in Histogram\test.txt") as f:
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
            print("Generated Output:", soln.largestRectangleArea(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass