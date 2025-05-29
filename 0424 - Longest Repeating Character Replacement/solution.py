class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        window_char_count = {}
        max_freq_seen = 0

        longest_len = 0

        l_ptr = 0
        for r_ptr in range(len(s)):
            window_char_count[s[r_ptr]] = window_char_count.get(s[r_ptr], 0) + 1
            max_freq_seen = max(max_freq_seen, window_char_count[s[r_ptr]])
            if (r_ptr - l_ptr + 1) - max_freq_seen > k:
                window_char_count[s[l_ptr]] -= 1
                l_ptr += 1
            longest_len = max(longest_len, r_ptr - l_ptr + 1)
        
        return longest_len
        
        
if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0424 - Longest Repeating Character Replacement\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line: 
                    line, k = line.split(", k = ")
                    ip.append([line.split(" = ")[1][1:-1], int(k)])
                elif "Output" in line: op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.characterReplacement(ip[i][0], ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass