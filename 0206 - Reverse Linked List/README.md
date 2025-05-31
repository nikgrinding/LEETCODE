# 206. Reverse Linked List

## Problem  
Given the `head` of a singly linked list, reverse the list and return the reversed list.

## Thought process  
We can reverse the list by iteratively changing the direction of the `next` pointer for each node as we move through the list.

## Approach  
- Initialize `new_head` as `None`  
- Traverse the list:  
  - Store the next node in a temp variable  
  - Reverse the current node's pointer to point to `new_head`  
  - Move `new_head` to the current node  
  - Move to the next node using the temp variable  
- Return `new_head` as the new head of the reversed list

## Complexity  
- Time: O(n)  
- Space: O(1)