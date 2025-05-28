class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1

        l_ptr, r_ptr = 0, len(nums1) - 1

        while True:

            mid1 = (l_ptr+r_ptr)//2
            mid2 = (len(nums1)+len(nums2))//2 - (mid1 + 1) - 1

            nums1_left_end = nums1[mid1] if mid1 >= 0 else float("-inf")
            nums1_right_beg = nums1[mid1+1] if mid1+1 < len(nums1) else float("inf")

            nums2_left_end = nums2[mid2] if mid2 >= 0 else float("-inf")
            nums2_right_beg = nums2[mid2+1] if mid2+1 < len(nums2) else float("inf")

            if nums1_left_end <= nums2_right_beg and nums2_left_end <= nums1_right_beg:
                if (len(nums1)+len(nums2)) % 2 != 0: return min(nums1_right_beg, nums2_right_beg)
                else: return (max(nums1_left_end, nums2_left_end) + min(nums1_right_beg, nums2_right_beg))/2
            
            elif nums1_left_end < nums2_right_beg: l_ptr = mid1 + 1
            
            else: r_ptr = mid1 - 1

if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0004 - Median of Two Sorted Arrays\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l1_str, l2_str = line.split(", ")
                    l1_str = l1_str.split()[-1]
                    l2_str = l2_str.split()[-1]
                    l1_list = [int(i) for i in l1_str[1:-1].split(",")]
                    l2_list = [int(i) for i in l2_str[1:-1].split(",")]
                    ip.append([l1_list, l2_list])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.findMedianSortedArrays(ip[i][0], ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass