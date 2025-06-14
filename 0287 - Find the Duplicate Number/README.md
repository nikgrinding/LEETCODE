# 287. Find the Duplicate Number

## Problem
You are given an array of integers `nums` containing `n + 1` integers where each integer is between `1` and `n` (inclusive). There is only **one repeated number**, but it could be repeated more than once. Return this duplicate number without modifying the array and using only constant extra space.

## Thought process
We interpret the array as a linked list where each index points to `nums[i]`. The duplicate number causes a cycle in this "linked list". We use Floyd’s Tortoise and Hare algorithm to detect the cycle and find its entry point, which is the duplicate number.

## Approach
- Use two pointers, `slow` and `fast`, to detect a cycle:
  - `slow` moves one step at a time: `slow = nums[slow]`
  - `fast` moves two steps at a time: `fast = nums[nums[fast]]`
  - They meet inside the cycle
- Start a new pointer `duplicate` at the beginning
  - Move both `slow` and `duplicate` one step at a time until they meet
  - The meeting point is the duplicate number

## Complexity
- Time: O(n)
- Space: O(1)