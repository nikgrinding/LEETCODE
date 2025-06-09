# Definition for singly-linked list.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if head is None: return None

        temp = head
        while temp:
            new_node = Node(temp.val)
            new_node.next = temp.next
            temp.next = new_node
            temp = new_node.next
        
        temp = head
        while temp:
            if temp.random: temp.next.random = temp.random.next
            temp = temp.next.next
        
        temp = head
        copy_head = head.next
        while temp:
            copy = temp.next
            temp.next = temp.next.next
            if copy.next: copy.next = copy.next.next
            temp = temp.next
        
        return copy_head

def array_to_ll (head, randoms):
    new_head = Node(0)
    temp = new_head
    l = []
    for i in head:
        temp.next = Node(i)
        temp = temp.next
        l.append(temp)

    temp = new_head
    for i in range(len(randoms)):
        temp.next.random = l[randoms[i]] if randoms[i] != None else None
        temp = temp.next

    return new_head.next

def display (head):
    if not head: 
        print ("[]")
        return
    temp = head
    print("[", end = "")
    while temp.next:
        if temp.random: print("[" + str(temp.val) + "," + str(temp.random.val) + "]", end = ",")
        else: print("[" + str(temp.val) + "," + "None" + "]", end = ",")
        temp = temp.next
    if temp.random: print("[" + str(temp.val) + "," + str(temp.random.val) + "]", "]", sep = "")
    else: print("[" + str(temp.val) + "," + "None" + "]", "]", sep = "")
        
if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0138 - Copy List with Random Pointer\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    l_str = line.split()[-1]
                    l1_list = [int(i.split(",")[0]) for i in l_str[2:-2].split("],[")]
                    l2_list = [int(i.split(",")[1]) if i.split(",")[1].isnumeric() else None for i in l_str[2:-2].split("],[") ]
                    ip.append([l1_list, l2_list])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1])
            print("Expected Output:", op[i])
            print("Generated Output:", end = " ")
            display(soln.copyRandomList(array_to_ll(ip[i][0], ip[i][1])))
        print()

    except Exception as e:
        print(e)
        pass