class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2): return False

        s1_freq = [0]*26
        window_freq = [0]*26

        for i in range(len(s1)): 
            s1_freq[ord(s1[i]) - ord("a")] += 1
            window_freq[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26): matches += 1 if s1_freq[i] == window_freq[i] else 0

        l_ptr = 0
        for r_ptr in range(len(s1), len(s2)):
            if matches == 26: return True

            new_char_index = ord(s2[r_ptr]) - ord("a")
            if s1_freq[new_char_index] == window_freq[new_char_index]: matches -= 1
            window_freq[new_char_index] += 1
            if s1_freq[new_char_index] == window_freq[new_char_index]: matches += 1

            old_char_index = ord(s2[l_ptr]) - ord("a")
            if s1_freq[old_char_index] == window_freq[old_char_index]: matches -= 1
            window_freq[old_char_index] -= 1
            if s1_freq[old_char_index] == window_freq[old_char_index]: matches += 1
            
            l_ptr += 1
        
        return matches == 26

        
if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0567 - Permutation in String\test.txt") as f:
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
            print("Generated Output:", soln.checkInclusion(ip[i][0], ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass