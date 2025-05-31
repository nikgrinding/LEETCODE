# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        new_head = None

        while head:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp

        return new_head

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

        with open(r"LEETCODE\0206 - Reverse Linked List\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str = line.split()[-1]
                    l_list = [int(i) for i in l_str[1:-1].split(",") if i != ""]
                    ip.append(l_list)
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i])
            print("Expected Output:", op[i])
            print("Generated Output:", end = " ")
            display(soln.reverseList(array_to_ll(ip[i])))
        print()

    except Exception as e:
        print(e)
        pass