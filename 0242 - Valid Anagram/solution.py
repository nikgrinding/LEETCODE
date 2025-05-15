class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if (len(s) != len(t)): return False

        hash_table = [0]*26

        for i in range(len(s)):
            hash_table[ord(s[i]) - ord("a")] += 1
            hash_table[ord(t[i]) - ord("a")] -= 1

        for i in hash_table: 
            if i != 0: return False
        return True
        
if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0242 - Valid Anagram\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l = line.split(",")
                    l[0] = l[0].split("\"")[1]
                    l[1] = l[1].split("\"")[1]
                    ip.append(l)
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.isAnagram(ip[i][0], ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass