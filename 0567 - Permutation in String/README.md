# 567. Permutation in String

## Problem  
Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`, or `False` otherwise. In other words, return `True` if one of `s1`'s permutations is a substring of `s2`.

## Thought process  
Since we're checking if a permutation of `s1` appears in `s2`, we can use a sliding window of size `len(s1)` over `s2` and compare the character frequencies. If all 26 character counts match at any point, we know a valid permutation exists.

## Approach  

- Initialize two frequency arrays of size 26 for `s1` and the current window in `s2`
- Fill both arrays with initial counts from `s1` and the first `len(s1)` characters of `s2`
- Count how many character positions match between the two arrays
- Slide the window one character at a time:
  - Update the frequency for the new incoming character
  - Update the frequency for the outgoing character
  - Adjust the match count accordingly
- If at any point all 26 character frequencies match, return `True`
- After the loop, return whether all frequencies match

## Complexity  
- Time: O(n)  
- Space: O(1)