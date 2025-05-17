class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1 for i in range(len(nums))]

        pre_prod = 1
        for i in range(len(nums)):
            answer[i] *= pre_prod
            pre_prod *= nums[i]
        
        post_prod = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= post_prod
            post_prod *= nums[i]
        
        return answer

if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0238 - Product of Array Except Self\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str = line.split()[-1][1:-1]
                    l_list = [int(i) for i in l_str.split(",")]
                    ip.append(l_list)
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.productExceptSelf(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass