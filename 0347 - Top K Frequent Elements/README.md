# 347. Top K Frequent Elements

## Problem
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

## Thought Process
We can calculate the frequency of each unique element in `nums` and store it in a hashtable. We can then group all the elements with the same frequency in a list of buckets (i.e., using bucket sort). Finally, we iterate from the highest frequency to the lowest and collect the top `k` frequent elements.

## Approach
- Count the frequency of each element using a dictionary (acts as a hashtable)
- Create a list of empty lists where the index represents the frequency (i.e., bucket sort)
- Place elements into the bucket corresponding to their frequency
- Iterate over the buckets and collect elements in reverse and finally return `k` of them

## Complexity
- Time: O(n)
- Space: O(n)