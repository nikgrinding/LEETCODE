# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = ListNode()

        temp = head

        while list1 and list2:

            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next

            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next

        temp.next = list1 or list2
        
        return head.next

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

        with open(r"LEETCODE\0021 - Merge Two Sorted Lists\test.txt") as f:
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
            display(soln.mergeTwoLists(array_to_ll(ip[i][0]), array_to_ll(ip[i][1])))
        print()

    except Exception as e:
        print(e)
        pass