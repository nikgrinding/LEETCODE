class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        answer = 0

        l_ptr, r_ptr = 0, len(height)-1
        l_max, r_max = height[l_ptr], height[r_ptr]
        while l_ptr < r_ptr:
            if l_max < r_max:
                l_ptr += 1
                l_max = max(l_max, height[l_ptr])
                answer += l_max - height[l_ptr]
            else:
                r_ptr -= 1
                r_max = max(r_max, height[r_ptr])
                answer += r_max - height[r_ptr]
        
        return answer

if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0042 - Trapping Rain Water\test.txt") as f:
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
            print("Generated Output:", soln.trap(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass