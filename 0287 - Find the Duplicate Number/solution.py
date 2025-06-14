class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        slow, fast = 0, 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
        
        duplicate = 0
        while True:
            slow, duplicate = nums[slow], nums[duplicate]
            if slow == duplicate: return duplicate

if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0287 - Find the Duplicate Number\test.txt") as f:
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
            print("Generated Output:", soln.findDuplicate(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass