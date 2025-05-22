# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         string = ""
#         for i in s:
#             if i.isalpha(): string += i.lower()
#         return string == string[::-1]

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l_ptr, r_ptr = 0, len(s)-1
        while l_ptr < r_ptr:
            if not s[l_ptr].isalnum(): l_ptr += 1
            elif not s[r_ptr].isalnum(): r_ptr -= 1
            elif s[l_ptr].lower() != s[r_ptr].lower(): return False
            else:
                l_ptr += 1
                r_ptr -= 1
        return True

if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0125 - Valid Palindrome\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line: ip.append(line.split(" = ")[1][1:-2])
                elif "Output" in line: op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.isPalindrome(ip[i]))
        print()

    except Exception as e:
        print(e)
        pass