# 138. Copy List with Random Pointer

## Problem
You are given the `head` of a linked list where each node contains a `val`, a `next` pointer, and a `random` pointer that can point to any node or `None`. Return a **deep copy** of the list — a new list with the same structure and values but with all new nodes.

## Thought process
We need to duplicate each node and properly assign both `next` and `random` pointers, while ensuring no links point back to the original list. Using extra space (like a hash map) is straightforward, but we can do it with **O(1) extra space** by interleaving the copied nodes within the original list and then separating them.

## Approach
- Iterate through the original list and insert a copied node immediately after each original node
- Traverse the list again to assign `random` pointers for the copied nodes using the fact that `original.next` is the copied node
- Traverse a final time to separate the copied list from the original and restore the original structure

## Complexity
- Time: O(n)  
- Space:  
  - O(n) for the output (copied nodes)  
  - O(1) extra space