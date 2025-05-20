# 150. Evaluate Reverse Polish Notation

## Problem  
Evaluate the value of an arithmetic expression in **Reverse Polish Notation** (RPN).

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

Note:
- Division between two integers should truncate toward zero.
- The given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

## Thought process  
The expression is in postfix notation, so I can't evaluate it left-to-right directly. Instead, I use a stack to process numbers and apply operations. Whenever I see a number, I push it to the stack. When I see an operator, I pop the top two numbers, apply the operation, and push the result back. I repeat this until the expression is fully processed.

## Approach  
- Initialize an empty stack
- Loop through each token:
  - If the token is a number (including negative numbers), convert it to an integer and push it onto the stack
  - If it's an operator:
    - Pop the top two values from the stack (the second popped is the first operand)
    - Apply the operation based on the current operator
    - Push the result back to the stack
- After processing all tokens, the final result will be the last item in the stack

## Complexity  
- Time: O(n)
- Space: O(n)