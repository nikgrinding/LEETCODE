# 739. Daily Temperatures

## Problem  
Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, put `0` instead.

## Thought process  
I noticed that for each temperature, I needed to look forward to find the next warmer day. A brute force approach would be too slow, so I thought of using a monotonic stack to keep track of indices of unresolved days. Then I explored another approach that works in reverse and skips forward using previously computed answers, which is more like a DP-style solution.

## Approach  

### Approach 1: Monotonic Stack  
- Use a stack to store indices of days in decreasing temperature order  
- For each day:
  - While the current temperature is higher than the one at the index on top of the stack:
    - Pop the index and set `answer[index] = current_index - index`  
  - Push the current index to the stack  
- This way, each temperature is processed exactly once

### Approach 2: Reverse Iteration with Skipping (DP-like)  
- Iterate from the end of the array toward the beginning  
- Keep track of the hottest temperature seen so far  
- If the current temp is greater than or equal to the hottest, update the hottest and continue  
- Else:
  - Start from the next day and keep jumping ahead using the `answer` array until a warmer temp is found  
  - Update `answer[i]` with the total number of days skipped

## Complexity  

| Operation   | Time (Stack) | Time (Reverse) | Space (Stack) | Space (Reverse) |
|-------------|--------------|----------------|----------------|-----------------|
| Overall     | O(n)         | O(n)           | O(n)           | O(1) auxiliary  |

> Note: The reverse iteration approach is slightly more space-efficient as it avoids using extra data structures like a stack. Both approaches achieve the same time complexity.