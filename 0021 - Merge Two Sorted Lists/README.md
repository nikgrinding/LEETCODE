# 21. Merge Two Sorted Lists

## Problem
You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

## Thought process
Since both lists are already sorted, we can merge them by comparing elements one by one and attaching the smaller one to the result list. We can use a dummy head to simplify handling the result list.

## Approach
- Create a dummy `ListNode` to serve as the start of the merged list
- Use a `temp` pointer to build the merged list
- Traverse both lists, comparing their current node values
- Append the smaller node to `temp.next`, and move the pointer forward in the corresponding list
- Move `temp` forward
- Once one list is exhausted, attach the remaining part of the other list
- Return `head.next` as the merged list (since `head` is a dummy)

## Complexity
- Time: O(n + m)  
- Space: O(1)