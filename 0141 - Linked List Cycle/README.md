# 141. Linked List Cycle

## Problem
Given `head`, the head of a linked list, determine if the linked list has a cycle in it. A cycle exists if a node in the list can be reached again by continuously following the `next` pointer. Return `true` if there is a cycle, otherwise return `false`.

## Thought process
If we try to traverse a cyclic linked list normally, we’ll loop forever. To detect this without storing visited nodes, we can use two pointers moving at different speeds—if there's a cycle, they’ll eventually meet.

## Approach
- Initialize two pointers, `slow` and `fast`, both starting at `head`
- Move `slow` one step and `fast` two steps in each iteration
- If `slow` and `fast` ever meet, there's a cycle
- If `fast` or `fast.next` becomes `None`, we've reached the end, so there's no cycle

## Complexity
- Time: O(n)  
- Space: O(1)