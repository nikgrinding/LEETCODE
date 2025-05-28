# 4. Median of Two Sorted Arrays

## Problem  
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

## Thought process  
We want to find the median of two sorted arrays in logarithmic time. That means we need to avoid merging them and instead use binary search to find the correct partition point such that elements on both sides of the partition are valid to compute the median. To simplify edge cases, we always do binary search on the smaller array.

## Approach  

- Ensure `nums1` is the smaller array so we binary search on it
- Perform binary search on `nums1` to find a partition such that:
  - Left side max of `nums1` <= Right side min of `nums2`
  - Left side max of `nums2` <= Right side min of `nums1`
- At each step, compute left and right partition boundaries safely using `float('-inf')` and `float('inf')` for out-of-bound cases
- If we find a valid partition:
  - If total length is odd, median is the smaller of the right sides
  - If total length is even, median is the average of the larger of the left sides and smaller of the right sides

## Complexity  
- Time: O(log(min(m, n)))
- Space: O(1)