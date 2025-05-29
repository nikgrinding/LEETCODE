class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        last_seen = {}
        longest_len = 0

        l_ptr = 0
        for r_ptr in range(len(s)):
            if s[r_ptr] in last_seen and last_seen[s[r_ptr]] >= l_ptr:
                l_ptr = last_seen[s[r_ptr]] + 1
            last_seen[s[r_ptr]] = r_ptr
            longest_len = max(longest_len, r_ptr - l_ptr + 1)
        
        return longest_len

if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0003 - Longest Substring Without Repeating Characters\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line: ip.append(line.split(" = ")[1][1:-2])
                elif "Output" in line: op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.lengthOfLongestSubstring(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass