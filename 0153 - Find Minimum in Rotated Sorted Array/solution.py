class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l_ptr, r_ptr = 0, len(nums) - 1
        while l_ptr < r_ptr:
            mid = (l_ptr+r_ptr)//2
            if nums[mid] > nums[r_ptr]: l_ptr = mid + 1
            else: r_ptr = mid
        return nums[l_ptr]

if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0153 - Find Minimum in Rotated Sorted Array\test.txt") as f:
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
            print("Generated Output:", soln.findMin(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass