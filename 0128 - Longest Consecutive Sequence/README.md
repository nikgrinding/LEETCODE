# 128. Longest Consecutive Sequence

## Problem
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

## Thought Process

For each number, we can check if it could be the **start of a sequence**. If it is, we expand the sequence by checking its consecutive successors, as long as those numbers exist in the set. Meanwhile, we keep track of the maximum sequence length encountered.

## Approach
- Convert `nums` to a set to allow O(1) lookups
- Initialize a variable `answer` to track the maximum length
- Loop through each number in the set:
  - If `num - 1` is **not** in the set, this number is the start of a sequence
  - Keep checking and expanding the sequence by incrementing the number while it exists in the set
  - Update `answer` if the current sequence is longer than the previously recorded one
- Return `answer`

## Complexity
- Time: O(n)  
- Space: O(n)
