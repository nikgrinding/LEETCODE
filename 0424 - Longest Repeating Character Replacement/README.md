# 424. Longest Repeating Character Replacement

## Problem  
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character at most `k` times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Thought process  
We need to find the longest window where we can make all characters the same using at most `k` replacements. As we slide through the string, we can use the frequency of the most common character in the window to decide whether it's valid or needs to shrink.

## Approach  

- Use a sliding window with two pointers
- Maintain a count of all characters in the current window using a dictionary
- Track the frequency of the most common character seen so far in the window
- If the number of characters to change `(window length - max frequency)` exceeds `k`, move the left pointer to shrink the window
- Update the longest valid window length as we go

## Complexity  
- Time: O(n)  
- Space: O(26) i.e. O(1)