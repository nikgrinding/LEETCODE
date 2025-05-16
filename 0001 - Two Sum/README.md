# 1. Two Sum

## Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Thought process
While traversing the list, we can store each element and its index in a hash table. To check if there is another element that can add up to the target, we simply check whether the complement of the current element exists in the hash table.

## Approach
- Create a dictionary to act as a hashtable
- Traverse through each element in `nums`
- If the complement of the current element (`target` - element) exists in the hashtable, return the pair of indices otherwise add the element to the hashtable with the element as the key and its index as the value

## Complexity
- Time: O(n)
- Space: O(n)