# 153. Find Minimum in Rotated Sorted Array

## Problem  
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`. Given the rotated array `nums`, return the minimum element.

## Thought process  
Since the array is rotated and still sorted in parts, the minimum element lies at the pivot where the rotation happened. By comparing the middle element with the rightmost element, we can determine which side of the array contains the pivot. A binary search approach allows us to find this in logarithmic time.

## Approach  

- Initialize two pointers at the start and end of the array
- While the left pointer is less than the right:
  - Calculate the middle index
  - If the middle element is greater than the rightmost element, the minimum is to the right of mid
  - Otherwise, the minimum is at mid or to the left of mid
- When the loop ends, the left pointer points to the smallest element

## Complexity  
- Time: O(log n)  
- Space: O(1)