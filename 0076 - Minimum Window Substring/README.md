# 76. Minimum Window Substring

## Problem  
Given two strings `s` and `t`, return the minimum window in `s` which contains all the characters in `t`. If no such window exists, return an empty string. The characters in the window must have the same frequency as in `t`, and the order in `s` must be preserved.

## Thought process  
We need to find a window in `s` that contains all the characters of `t` with the right counts. A sliding window is ideal here since we can dynamically grow and shrink the window to find the minimum valid substring.

## Approach  

- Count the frequency of each character in `t`
- Use two pointers to define a window in `s` and track character frequencies in that window
- Move the right pointer to expand the window and include more characters
- When the window has all required characters with correct frequencies, try shrinking from the left to minimize it
- Track the smallest valid window during the process

## Complexity  
- Time: O(n + m)  
- Space: O(m)