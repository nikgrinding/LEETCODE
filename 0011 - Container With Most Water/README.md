# 11. Container With Most Water

## Problem  
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are at `(i, 0)` and `(i, height[i])`.  
Find two lines that together with the x-axis form a container, such that the container contains the most water.  
Return the maximum amount of water a container can store.

## Thought process  
The brute-force way is to try every pair of lines and compute the area, but that's too slow. Instead, I used the two-pointer technique, starting from both ends and always moving the pointer pointing to the shorter line - this ensures we don’t miss any potentially larger area as the width reduces.

## Approach  

- Initialize two pointers, one at the start and the other at the end of the array
- At each step, calculate the area using the current pair of lines
- Update the maximum area if the current one is larger
- Move the pointer pointing to the shorter line inward
- Repeat until both pointers meet

## Complexity  

- Time: O(n)  
- Space: O(1) 