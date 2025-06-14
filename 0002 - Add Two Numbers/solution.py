# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = ListNode(0)
        temp = head
        carry = 0

        while l1 or l2:

            new_node_value = 0

            if l1: new_node_value += l1.val
            if l2: new_node_value += l2.val

            new_node_value += 1 if carry else 0

            carry = 1 if new_node_value > 9 else 0
            new_node_value = new_node_value % 10

            temp.next = ListNode(new_node_value)

            temp = temp.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry: temp.next = ListNode(carry)

        return head.next

def array_to_ll (head):
    new_head = ListNode(0)
    new_node = new_head
    for i in head:
        new_node.next = ListNode(i)
        new_node = new_node.next
    return new_head.next

def display (head):
    if not head: 
        print ("[]")
        return
    new_node = head
    print("[", end = "")
    while new_node.next:
        print(new_node.val, end = ",")
        new_node = new_node.next
    print(new_node.val, "]", sep = "")       
        
if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0002 - Add Two Numbers\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l1_str, l2_str = line.split(", ")
                    l1_str = l1_str.split()[-1]
                    l2_str = l2_str.split()[-1]
                    l1_list = [int(i) for i in l1_str[1:-1].split(",") if i != ""]
                    l2_list = [int(i) for i in l2_str[1:-1].split(",") if i != ""]
                    ip.append([l1_list, l2_list])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1])
            print("Expected Output:", op[i])
            print("Generated Output:", end = " ")
            display(soln.addTwoNumbers(array_to_ll(ip[i][0]), array_to_ll(ip[i][1])))
        print()

    except Exception as e:
        print(e)
        pass