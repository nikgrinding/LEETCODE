# 49. Group Anagrams

## Problem
Given an array of strings `strs`, group the anagrams together.

## Thought process
Two strings are anagrams if they have the same length and the frequency of each character in both strings is identical. So, we can create a hashtable to store the frequency of characters in each string and then use this to group them.

## Approach
- Create a dictionary to act as a hashtable
- Traverse through each string in `strs`
- For each string, calculate the frequency of its characters and use this frequency as the key in the hash table
- If the key exists, append the string to its value
- If not, add a new entry in the hash table with the frequency as the key and the string in a new list as the value

## Complexity
- Time: O(n*k)
- Space: O(n*k)
{where k is the length of the longest string in `strs`}