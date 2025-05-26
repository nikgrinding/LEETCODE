import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        l_ptr, r_ptr = 1, max(piles)
        answer = r_ptr

        while l_ptr <= r_ptr:

            mid = (l_ptr+r_ptr)//2

            temp_time = 0
            for pile in piles: temp_time += math.ceil(pile/mid)

            if temp_time <= h:
                answer = mid
                r_ptr = mid - 1
            else:
                l_ptr = mid + 1
        
        return answer
        

if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0875 - Koko Eating Bananas\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str, hours = line.split(", ")
                    l_str = l_str.split()[-1]
                    l_list = [int(i) for i in l_str[1:-1].split(",")]
                    hours = int(hours.split()[-1])
                    ip.append([l_list, hours])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.minEatingSpeed(ip[i][0], ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass