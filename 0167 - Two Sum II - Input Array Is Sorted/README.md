# 167. Two Sum II - Input Array Is Sorted

## Problem  
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific target number. Return the indices of the two numbers (1-indexed) as an integer array `answer` of length 2. You may not use the same element twice. You must solve it using only constant extra space.

## Thought process  
Since the array is already sorted, I realized we could use a two-pointer approach: one starting from the beginning and the other from the end. If the sum is greater than the target, we move the right pointer leftward to reduce the sum. If it's less, we move the left pointer to increase the sum. This guarantees a solution in one pass without using extra space.

## Approach  

- Initialize two pointers: one at the start and one at the end  
- While the sum is not equal to the target:
  - If the sum is too high, move the right pointer left
  - If the sum is too low, move the left pointer right  
- When the sum matches the target, return the 1-indexed positions of both pointers  

## Complexity  

Time: O(n)  
Space: O(1)  