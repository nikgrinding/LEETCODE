# class MinStack(object):

#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         self.stack.append(val)
#         if not self.min_stack or self.min_stack[-1] > val: self.min_stack.append(val)
#         else: self.min_stack.append(self.min_stack[-1])

#     def pop(self):
#         """
#         :rtype: None
#         """
#         self.stack.pop()
#         self.min_stack.pop()

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.min_stack[-1]

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val - self.min < 0: self.min = val

    def pop(self):
        """
        :rtype: None
        """
        ele = self.stack.pop()
        if ele < 0: self.min -= ele

    def top(self):
        """
        :rtype: int
        """
        ele = self.stack[-1]
        if ele > 0: return ele + self.min
        else: return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0155 - Min Stack\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    ip.append(line.split(": ")[-1])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        print("\nInput:", ip[0])
        print("Expected Output:", op[0])
        obj = MinStack()
        gop = [obj.push(-2), obj.push(0), obj.push(-3), obj.getMin(), obj.pop(), obj.top(), obj.getMin()]
        print("Generated Output:", gop)
        print()

    except Exception as e:
        print(e)
        pass