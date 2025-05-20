# 155. Min Stack

## Problem  
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `push(int val)` – Pushes the element onto the stack.
- `pop()` – Removes the element on the top of the stack.
- `top()` – Gets the top element.
- `getMin()` – Retrieves the minimum element in the stack.

All operations must be implemented in **O(1)** time complexity.

## Thought process  
To get the minimum element in constant time, I realized we need to store additional information with each push. My first approach was to use a second stack to keep track of the minimum value at every level. Later, I explored a more space-optimized approach using just one stack by storing the difference between the value and the current minimum.

## Approach  

### Approach 1: Two Stacks  
- Use two stacks:
  - One for actual values
  - One for the minimum value at each level
- When pushing:
  - Push value to the main stack
  - Push `min(current_val, current_min)` to the min stack
- When popping:
  - Pop from both stacks
- `top()` gives top of the main stack
- `getMin()` gives top of the min stack

### Approach 2: Single Stack with Encoded Differences  
- Use one stack to store `val - min` instead of the actual value
- Track the current minimum in a separate variable
- When pushing:
  - If the stack is empty, push `0` and set `min = val`
  - Else, push `val - min` and update `min` if `val` is smaller
- When popping:
  - If the popped value is negative, it means we popped the current minimum
  - Restore the previous minimum using this negative value
- To get the actual `top()`, decode using `min`
- `getMin()` just returns the current `min`

## Complexity  

| Operation   | Time (Two Stacks) | Time (Single Stack) | Space (Two Stacks) | Space (Single Stack) |
|-------------|-------------------|----------------------|---------------------|----------------------|
| push        | O(1)              | O(1)                 | O(n)                | O(n)                 |
| pop         | O(1)              | O(1)                 | O(n)                | O(n)                 |
| top         | O(1)              | O(1)                 | O(n)                | O(n)                 |
| getMin      | O(1)              | O(1)                 | O(n)                | O(1) auxiliary       |

> Note: The single-stack approach is slightly more space-efficient in terms of **auxiliary storage**, especially if values are large or memory-constrained.