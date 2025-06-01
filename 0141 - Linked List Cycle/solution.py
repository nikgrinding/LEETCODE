# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False

def array_to_ll (head, pos):
    new_head = ListNode(0)
    temp = new_head
    l = []
    for i in head:
        temp.next = ListNode(i)
        temp = temp.next
        l.append(temp)
    if pos != -1: temp.next = l[pos]
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

        with open(r"LEETCODE\0141 - Linked List Cycle\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str, pos = line.split(": ")[-1].split(", ")
                    l_str = l_str.split()[-1]
                    pos = int(pos.split()[-1])
                    l_list = [int(i) for i in l_str[1:-1].split(",") if i != ""]
                    ip.append([l_list, pos])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.hasCycle(array_to_ll(ip[i][0], ip[i][1])))
        print()

    except Exception as e:
        print(e)
        pass