# 74. Search a 2D Matrix

## Problem  
You are given an `m x n` integer matrix `matrix` with the following properties:  
- Each row is sorted in non-decreasing order  
- The first integer of each row is greater than the last integer of the previous row  

Given an integer `target`, return `True` if `target` is in `matrix`, or `False` otherwise.

## Thought process  
The matrix has a sorted structure when viewed as a flattened 1D array. So instead of treating it as a 2D grid, I treated it like a single sorted array of length `m × n`. This allows for a clean binary search solution using index conversion to get back the original row and column.

## Approach  

- Compute total number of rows `r` and columns `c`
- Use binary search on a virtual 1D array of length `r * c`
- At each iteration:
  - Convert the mid index to 2D using `(mid // c, mid % c)`
  - If the value equals target, return `True`
  - If it's less than the target, move the left pointer right
  - If it's greater, move the right pointer left
- If the loop ends, return `False`

## Complexity  
- Time: O(log(m × n))  
- Space: O(1)