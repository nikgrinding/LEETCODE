# 238. Product of Array Except Self

## Problem
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

## Thought process
We can calculate the **prefix product** (i.e., the product of all the elements before the current element) and the **postfix product** (i.e., the product of all the elements after the current element) for each element. By multiplying the prefix and postfix products for each index, we get the final result.

## Approach
- Initialize the `answer` array with `1`s of the same length as `nums`.
- Perform a forward pass to compute the prefix product for each element:
  - For each index `i`, store the product of all elements before it in `answer[i]`.
- Perform a backward pass to compute the postfix product:
  - Multiply each element in `answer[i]` by the product of all elements after index `i`.

## Complexity
- Time: O(n)
- Space: O(1)