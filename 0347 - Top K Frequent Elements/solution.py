class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashtable = {}
        for i in nums:
            if i not in hashtable: hashtable[i] = 1
            else: hashtable[i] += 1

        freq = [[] for _ in range(len(nums))]
        for i in hashtable:
            freq[hashtable[i]-1] += [i]
        
        result = []
        for i in freq[::-1]: result.extend(i)
        return result[:k]
        

if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0347 - Top K Frequent Elements\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str, k = line.split(", ")
                    l_str = l_str.split()[-1]
                    l_list = [int(i) for i in l_str[1:-1].split(",")]
                    k = int(k.split()[-1])
                    ip.append([l_list, k])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.topKFrequent(ip[i][0], ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass