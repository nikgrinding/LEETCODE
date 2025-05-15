# 217. Contains Duplicate

## Problem
Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.

## Thought process
If the array contains any duplicates, then converting it to a set reduces its size. So, by comparing the length of the set and the original list we can determine if the list contains any duplicates.

## Approach
- Convert the list into a set and compare its length with the length of the original list

## Complexity
- Time: O(n)
- Space: O(n)