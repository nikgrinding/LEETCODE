# 84. Largest Rectangle in Histogram

## Problem  
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

## Thought process  
The challenge is to efficiently compute the largest area formed by one or more contiguous bars in the histogram. A brute-force approach that checks all possible rectangles would be too slow, so I used a monotonic increasing stack to track indices of bars. This helps identify boundaries where each bar can extend to the left and right while still being the smallest in that range.

## Approach  
- Use a stack to maintain indices of increasing bar heights  
- For each bar, if it is shorter than the bar on top of the stack, pop from the stack and calculate the area where the popped bar is the smallest bar  
- The width is calculated based on the difference between the current index and the index left in the stack after popping  
- Append a dummy bar of height 0 at the end to flush out remaining bars in the stack  

## Complexity  
- Time: O(n)  
- Space: O(n)