# 242. Valid Anagram

## Problem
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

## Thought Process
Two strings are anagrams if they have the same length and the frequency of each character in both strings is identical. So, we can create a hashtable to store the frequency difference of each character and check if all the values are zero.

## Approach
- Check if lengths of `s` and `t` are different. If so, return `False`.
- Create a list (acts as hashtable) of size 26.
- Traverse both strings simultaneously:
  - Increment the count for the character in `s`.
  - Decrement the count for the character in `t`.
- If all values in the frequency list are zero, return `True`. Otherwise, return `False`.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)