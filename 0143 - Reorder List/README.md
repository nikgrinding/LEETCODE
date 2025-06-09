# 143. Reorder List

## Problem
You are given the head of a singly linked list. Reorder the list so that the nodes are arranged in this specific order: first node → last node → second node → second last node → and so on. You must do this in-place without altering the node values.

## Thought process
To reorder the list as described, we can split the list into two halves, reverse the second half, and then merge the two halves alternately.

## Approach
- Use the slow and fast pointer technique to find the middle of the list
- Split the list into two halves by setting `slow.next = None`
- Reverse the second half of the list
- Merge the first half and the reversed second half by alternating nodes

## Complexity
- Time: O(n)  
- Space: O(1)