class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        r, c = len(matrix), len(matrix[0])
        l_ptr, r_ptr = 0, r*c - 1
        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr)//2
            if matrix[mid//c][mid%c] == target: return True
            elif matrix[mid//c][mid%c] < target: l_ptr = mid + 1
            else: r_ptr = mid - 1
        return False
        

if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0074 - Search a 2D Matrix\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str, target = line.split(", ")
                    l_str = l_str.split()[-1]
                    l_str = l_str[2:-2].split("],[")
                    l_list = [[int(j) for j in i.split(",")] for i in l_str]
                    target = int(target.split()[-1])
                    ip.append([l_list, target])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.searchMatrix(ip[i][0], ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass