class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(t) > len(s): return ""

        t_char_freq = {}
        for char in t: t_char_freq[char] = t_char_freq.get(char, 0) + 1

        window_char_freq = {}
        have, need = 0, len(t_char_freq)
        smallest_window_ptrs, smallest_window_length = [-1, -1], float("inf")

        l_ptr = 0
        for r_ptr in range(len(s)):

            char = s[r_ptr]
            window_char_freq[char] = window_char_freq.get(char, 0) + 1

            if t_char_freq.get(char, 0) == window_char_freq[char]: have += 1

            while have == need:
                if r_ptr - l_ptr + 1 < smallest_window_length:
                    smallest_window_ptrs = [l_ptr, r_ptr]
                    smallest_window_length = r_ptr - l_ptr + 1
                window_char_freq[s[l_ptr]] -= 1
                if window_char_freq[s[l_ptr]] < t_char_freq.get(s[l_ptr], 0): have -= 1
                l_ptr+=1

        return s[smallest_window_ptrs[0]: smallest_window_ptrs[1]+1] if smallest_window_length != float("inf") else ""

        
if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0076 - Minimum Window Substring\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line: 
                    str1, str2  = line.split(", ")
                    ip.append([str1.split(" = ")[1][1:-1], str2.split(" = ")[1][1:-2]])
                elif "Output" in line: op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.minWindow(ip[i][0], ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass