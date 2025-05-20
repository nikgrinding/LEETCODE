# 20. Valid Parentheses

## Problem  
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.  
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.

## Thought process  
I thought of using a stack to keep track of the opening brackets. As I go through the string, I push opening brackets into the stack. For closing brackets, I check if the top of the stack matches the corresponding opening bracket. If at any point it doesn’t match or the stack is empty when it shouldn’t be, the string is invalid.

## Approach  
- Use a stack to store opening brackets.
- Use a dictionary to map closing brackets to their matching opening ones.
- Traverse the string:
  - Push opening brackets to the stack.
  - For closing brackets, check if the top of the stack has the matching opening bracket. If it does, pop it. If not, return false.
- In the end, return true if the stack is empty (all brackets matched), else false.

## Complexity  
- Time: O(n)  
- Space: O(n)