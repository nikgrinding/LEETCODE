# 2. Add Two Numbers

## Problem
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the result as a linked list, also in reverse order.

## Thought process
We simulate digit-by-digit addition like elementary school, starting from the least significant digit. If the sum of two digits is greater than 9, we carry over 1 to the next position.

## Approach
- Create a dummy head to build the result list
- Use a `carry` variable to track carry-over from the previous addition
- Traverse both input lists, summing the digits and carry
- Create a new node for each digit of the sum and append it to the result list
- After the loop, if a carry remains, add one more node

## Complexity
- Time: O(n)  
- Space: O(1)