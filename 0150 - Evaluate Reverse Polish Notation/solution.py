class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i.isnumeric() or i[1:].isnumeric(): stack.append(int(i))
            else:
                y, x = stack.pop(), stack.pop()
                if i == "+": stack.append(x + y)
                elif i == "-": stack.append(x - y)
                elif i == "*": stack.append(x * y)
                else: stack.append(int(x/y))
        return stack.pop()

if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0150 - Evaluate Reverse Polish Notation\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str = line.split()[-1][1:-1]
                    l_list = [i[1:-1] for i in l_str.split(",")]
                    ip.append(l_list)
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.evalRPN(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass