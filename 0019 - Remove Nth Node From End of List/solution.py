# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0, head)

        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        
        return dummy.next

def array_to_ll (head):
    new_head = ListNode(0)
    temp = new_head
    for i in head:
        temp.next = ListNode(i)
        temp = temp.next
    return new_head.next

def display (head):
    if not head: 
        print ("[]")
        return
    temp = head
    print("[", end = "")
    while temp.next:
        print(temp.val, end = ",")
        temp = temp.next
    print(temp.val, "]", sep = "")
        
if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0019 - Remove Nth Node From End of List\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str, target = line.split(", ")
                    l_str = l_str.split()[-1]
                    l_list = [int(i) for i in l_str[1:-1].split(",")]
                    target = int(target.split()[-1])
                    ip.append([l_list, target])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1])
            print("Expected Output:", op[i])
            print("Generated Output:", end = " ")            
            display(soln.removeNthFromEnd(array_to_ll(ip[i][0]), ip[i][1]))
        print()

    except Exception as e:
        print(e)
        pass