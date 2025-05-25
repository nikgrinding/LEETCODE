# 704. Binary Search

## Problem  
Given a sorted array of integers `nums` and an integer `target`, return the index of `target` if it exists in the array. If not, return -1.

## Thought process  
Since the array is sorted, binary search is the most efficient way to find the target. I decided to use two pointers and check the middle element in each iteration, narrowing down the search space based on comparisons.

## Approach  

- Initialize two pointers at the start and end of the array
- While the left pointer is less than or equal to the right:
  - Calculate the mid index
  - If the mid element matches the target, return its index
  - If the mid element is less than the target, search the right half
  - If the mid element is greater than the target, search the left half
- If not found, return -1

## Complexity  
- Time: O(log n)  
- Space: O(1)