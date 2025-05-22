# 125. Valid Palindrome

## Problem  
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

## Thought process  
I realized that we only need to compare characters that are letters or digits and ignore everything else. One way to approach this is to clean the string first and then check if it's the same forward and backward. Another way is to use two pointers from both ends and skip any non-alphanumeric characters while comparing.

## Approach  

### Approach 1: Clean and Compare  
- Iterate through the string and build a new lowercase string containing only alphanumeric characters  
- Compare the cleaned string with its reverse  

### Approach 2: Two-Pointer Technique  
- Use two pointers from both ends of the string  
- Skip non-alphanumeric characters  
- Compare characters at both pointers (case-insensitively)  
- If all matching pairs are equal, it's a palindrome  

## Complexity  

| Approach        | Time  | Space |
|-----------------|-------|-------|
| Clean & Compare | O(n)  | O(n)  |
| Two-Pointer     | O(n)  | O(1)  |