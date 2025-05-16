class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashtable = {}
        for string in strs:
            l = [0]*26
            for char in string: l[ord(char) - ord('a')] += 1
            key = tuple(l)
            if key not in hashtable: hashtable[key] = [string]
            else: hashtable[key].append(string)
        return list(hashtable.values()) 

if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0049 - Group Anagrams\test.txt") as f:
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
            print("Generated Output:", soln.groupAnagrams(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass