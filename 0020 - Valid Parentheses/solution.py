class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        complement = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in ["(", "[", "{"]: stack.append(i)
            else:
                if len(stack) == 0 or stack[-1] != complement[i]: return False
                stack.pop()
        return len(stack) == 0
        
if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0020 - Valid Parentheses\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line: ip.append(line.split(" = ")[1][1:-2])
                elif "Output" in line: op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.isValid(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass