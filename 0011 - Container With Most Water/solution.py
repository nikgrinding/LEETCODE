class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        answer = 0

        l_ptr, r_ptr = 0, len(height) - 1
        while l_ptr < r_ptr:
            temp_area = min(height[l_ptr], height[r_ptr]) * (r_ptr-l_ptr)
            answer = max(answer, temp_area)
            if height[l_ptr] < height[r_ptr]: l_ptr += 1
            else: r_ptr -= 1
        
        return answer 

if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0011 - Container With Most Water\test.txt") as f:
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
            print("Generated Output:", soln.maxArea(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass