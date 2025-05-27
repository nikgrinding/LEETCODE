# 981. Time Based Key-Value Store

## Problem  
Design a time-based key-value data structure that can store multiple values for the same key at different timestamps and retrieve the value of a key at a given timestamp. Implement the `TimeMap` class:
- `set(key, value, timestamp)` stores the key and value along with the given timestamp.
- `get(key, timestamp)` returns the value such that `set(key, value, timestamp_prev)` was called previously with `timestamp_prev <= timestamp`, and `timestamp_prev` is the largest possible. If there are no such values, return `""`.

## Thought process  
We need to store values in a way that allows efficient retrieval of the most recent value at or before a given timestamp. Using a dictionary to map keys to a list of `[value, timestamp]` pairs (stored in increasing order of timestamp), we can binary search for the correct timestamp.

## Approach  

- Use a dictionary to map each key to a list of `[value, timestamp]` pairs
- For `set`:
  - If the key is new, initialize its list
  - Append the `[value, timestamp]` pair to the key’s list
- For `get`:
  - If the key doesn't exist, return an empty string
  - Otherwise, perform binary search on the key’s list to find the largest timestamp ≤ given timestamp
  - Track and return the corresponding value

## Complexity  
- Time:  
  - `set`: O(1)  
  - `get`: O(log n), where n is the number of entries for the key  
- Space: O(n)