# 22. Generate Parentheses

## Problem  
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Thought process  
We want to create only valid strings made of `n` opening and `n` closing brackets. A string is valid only when each opening bracket has a matching closing bracket, and no closing bracket appears before its corresponding opening one.

## Approach  

### Approach 1: Backtracking  
- Use recursion to build strings character by character
- Add an opening bracket if total used is less than `n`
- Add a closing bracket only if it won’t exceed the number of opening ones used so far
- Add the string to the result once its length becomes `2n`

### Approach 2: Dynamic Programming  
- Let `dp[i]` be the list of valid combinations for `i` pairs of parentheses
- For each `i`, combine strings in the form: `"(" + dp[j] + ")" + dp[i - 1 - j]` for every `j` from `0` to `i - 1`
- Build up results from `dp[0]` to `dp[n]` using smaller solutions

## Complexity  

| Metric       | Backtracking         | Dynamic Programming     |
|--------------|----------------------|--------------------------|
| Time         | O(4^n / sqrt(n))     | O(4^n / sqrt(n))         |
| Space        | O(4^n / sqrt(n))     | O(4^n / sqrt(n))         |