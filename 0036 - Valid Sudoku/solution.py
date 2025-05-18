class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        subboxes = [set() for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                ele = board[i][j]
                if ele == ".": continue
                if ele in rows[i] or ele in cols[j] or ele in subboxes[3*(i//3) + j//3]: return False
                rows[i].add(ele)
                cols[j].add(ele)
                subboxes[3*(i//3) + j//3].add(ele)
        
        return True
        
if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0036 - Valid Sudoku\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str = line.split()[-1]
                    l_str = l_str[2:-2].split("],[")
                    for i in range(len(l_str)):
                        l_str[i] = l_str[i][1:-1].split("\",\"")
                    ip.append(l_str)
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:")
            for row in ip[i]:
                print(row)
            print("Expected Output:", op[i])
            print("Generated Output:", soln.isValidSudoku(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass