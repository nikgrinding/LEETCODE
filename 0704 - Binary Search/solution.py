class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l_ptr, r_ptr = 0, len(nums) - 1
        while l_ptr <= r_ptr:
            mid = (l_ptr + r_ptr)//2
            if nums[mid] == target: return mid
            elif nums[mid] < target: l_ptr = mid + 1
            else: r_ptr = mid - 1
        return -1
        

if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0704 - Binary Search\test.txt") as f:
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
            print("Generated Output:", soln.search(ip[i][0], ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass