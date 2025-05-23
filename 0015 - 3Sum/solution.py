class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answer = []

        nums.sort()

        for i in range(len(nums)):

            if i > 0 and nums[i]==nums[i-1]: continue

            l_ptr, r_ptr = i+1, len(nums)-1
            while l_ptr < r_ptr:
                temp_sum = nums[i] + nums[l_ptr] + nums[r_ptr]
                if temp_sum == 0:
                    answer.append([nums[i], nums[l_ptr], nums[r_ptr]])
                    l_ptr += 1
                    r_ptr -= 1
                    while l_ptr < r_ptr and nums[l_ptr-1] == nums[l_ptr]: l_ptr += 1
                    while l_ptr < r_ptr and nums[r_ptr+1] == nums[r_ptr]: r_ptr -= 1
                elif temp_sum < 0: l_ptr += 1
                else: r_ptr -= 1
        
        return answer
        
if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0015 - 3Sum\test.txt") as f:
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
            print("Generated Output:", soln.threeSum(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass