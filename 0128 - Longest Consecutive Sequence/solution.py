class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        hashset = set(nums)

        for i in hashset:
            if i-1 not in hashset:
                curr_len = 1
                while i+1 in hashset:
                    curr_len += 1
                    i = i+1
                answer = max(answer, curr_len)
        return answer

if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0128 - Longest Consecutive Sequence\test.txt") as f:
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
            print("Generated Output:", soln.longestConsecutive(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass