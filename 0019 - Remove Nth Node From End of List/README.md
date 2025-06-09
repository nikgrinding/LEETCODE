# 19. Remove Nth Node From End of List

## Problem
Given the head of a linked list, remove the `n`th node from the end of the list and return its head.

## Thought process
We need to identify the node just before the `n`th node from the end. A two-pointer technique can help by offsetting one pointer by `n` steps so that when it reaches the end, the other is right before the node to remove.

## Approach
- Use a dummy node pointing to the head to simplify edge cases
- Initialize two pointers: `left` at dummy and `right` at head
- Move `right` forward by `n` steps
- Move both `left` and `right` forward until `right` reaches the end
- `left` now points to the node before the one to remove
- Skip the target node by setting `left.next = left.next.next`
- Return `dummy.next` as the new head

## Complexity
- Time: O(n)  
- Space: O(1)