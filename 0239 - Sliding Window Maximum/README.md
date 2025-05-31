# 239. Sliding Window Maximum

## Problem  
You are given an array of integers `nums`, and there is a sliding window of size `k` which moves from the very left to the very right. You can only see the `k` numbers in the window. Return the maximum in each sliding window.

## Thought process  
We want to efficiently find the maximum in each window without scanning the full window every time. A deque helps track indices of useful elements — we maintain it in decreasing order of values so that the front always gives the max.

## Approach  
- Use a deque to store indices of potential maximum elements in decreasing order  
- For each element:
  - Remove indices from the back whose values are smaller than the current value (they can't be maximum anymore)  
  - Add current index to the deque  
  - If the front is out of the window, remove it  
  - Once the window has reached size `k`, append the value at the front of the deque to the result

## Complexity  
- Time: O(n)  
- Space: O(k)