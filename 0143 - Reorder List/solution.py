# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half_head = slow.next
        slow.next = None

        rev_second_half_head = None
        while second_half_head:
            temp = second_half_head.next
            second_half_head.next = rev_second_half_head
            rev_second_half_head = second_half_head
            second_half_head = temp
        
        while rev_second_half_head:
            temp1, temp2 = head.next, rev_second_half_head.next
            head.next = rev_second_half_head
            rev_second_half_head.next = temp1
            head, rev_second_half_head = temp1, temp2

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

        with open(r"LEETCODE\0143 - Reorder List\test.txt") as f:
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
            head = array_to_ll(ip[i])
            soln.reorderList(head)
            display(head)
        print()

    except Exception as e:
        print(e)
        pass