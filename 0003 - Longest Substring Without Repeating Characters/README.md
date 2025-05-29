# 3. Longest Substring Without Repeating Characters

## Problem  
Given a string `s`, find the length of the longest substring without repeating characters.

## Thought process  
We need to find the longest window in the string where all characters are unique. A sliding window approach works best here by expanding the window with a right pointer and shrinking it with a left pointer whenever a duplicate character is found.

## Approach  

- Use two pointers to represent a sliding window and a hash map to store the last seen index of each character
- Initialize `l_ptr` at the start and iterate `r_ptr` through the string
- If the current character was seen before and its last index is within the current window, move `l_ptr` just after that index
- Update the longest length after checking each character
- Return the longest window size found

## Complexity  
- Time: O(n)  
- Space: O(n)