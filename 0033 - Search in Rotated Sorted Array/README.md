# 33. Search in Rotated Sorted Array

## Problem  
You are given an integer array `nums` sorted in ascending order (with distinct values), which is rotated at an unknown pivot index. You are also given an integer `target`. If `target` is in `nums`, return its index. Otherwise, return -1.

## Thought process  
Even though the array is rotated, one half of the array (left or right) is still guaranteed to be sorted. By identifying which half is sorted and checking if the target lies within that sorted half, we can use binary search to discard the irrelevant half in each iteration.

## Approach  

- Initialize two pointers at the start and end of the array
- While the left pointer is less than or equal to the right:
  - Calculate the mid index
  - If the mid element matches the target, return its index
  - If the left side is sorted:
    - If the target lies within the sorted left half, move the right pointer
    - Otherwise, move the left pointer
  - If the right side is sorted:
    - If the target lies within the sorted right half, move the left pointer
    - Otherwise, move the right pointer
- If not found, return -1

## Complexity  
- Time: O(log n)  
- Space: O(1)