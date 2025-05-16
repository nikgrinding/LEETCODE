class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for index in range(len(nums)):
            if target - nums[index] in hash_table:
                return [hash_table[target - nums[index]], index]
            hash_table[nums[index]] = index

if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0001 - Two Sum\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str, target = line.split(", ")
                    l_str = l_str.split()[-1]
                    l_list = [int(i) for i in l_str[1:-1].split(",")]
                    target = int(target.split()[-1])
                    ip.append([l_list, target])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.twoSum(ip[i][0], ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass