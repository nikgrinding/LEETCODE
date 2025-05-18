# 36. Valid Sudoku

## Problem
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note: 
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated.

## Thought process
To ensure that the Sudoku board is valid, we need to check that:
- No duplicate digit appears in any row
- No duplicate digit appears in any column
- No duplicate digit appears in any of the 3×3 sub-boxes

We can use hash sets to keep track of the digits seen so far in each row, column, and sub-box as we iterate through the board.

## Approach
- Initialize three lists of sets: `rows`, `cols`, and `subboxes`, each of length 9
- Traverse the entire board using two nested loops (row `i` and column `j`)
- For each filled cell:
  - Check if the digit exists in the current row, column, or 3×3 sub-box set
  - If it does, return `False` (invalid Sudoku)
  - Otherwise, add the digit to the corresponding sets
- If no duplicates are found after traversing the whole board, return `True`

## Complexity
- Time: O(1)  
  (The board size is fixed at 9x9, so the iteration and operations are constant time.)
- Space: O(1)  
  (Using 27 sets to track digits — constant space due to fixed board size.)
