from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        answer = []

        queue = deque()

        l_ptr = 0
        for r_ptr in range(len(nums)):
            while queue and nums[r_ptr] > nums[queue[-1]]: queue.pop()
            queue.append(r_ptr)
            if queue[0] < l_ptr: queue.popleft()
            if r_ptr >= k-1:
                answer.append(nums[queue[0]])
                l_ptr += 1

        return answer
        

if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0239 - Sliding Window Maximum\test.txt") as f:
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
            print("Generated Output:", soln.maxSlidingWindow(ip[i][0], ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass