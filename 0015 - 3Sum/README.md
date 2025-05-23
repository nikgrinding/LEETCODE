# 15. 3Sum

## Problem  
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.  
The solution set must not contain duplicate triplets.

## Thought process  
The brute-force idea of checking all combinations is too slow. So I realized I can sort the array and fix one number, then use the two-pointer technique to find the remaining two numbers. This avoids duplicates and improves performance.

## Approach  

- Sort the array first
- Iterate through the array and fix one number `nums[i]`
- Use two pointers, one starting from `i + 1` and the other from the end
- Move pointers inward based on the sum compared to 0
- Skip duplicates to avoid repeated triplets

## Complexity  

- Time: O(n²)  
- Space: O(1) (ignoring the output list)