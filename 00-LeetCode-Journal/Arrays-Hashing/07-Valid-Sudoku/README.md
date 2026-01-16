# Valid Sudoku

## Problem

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

## Solution Approach: Hash Sets

We can iterate through the entire `9 x 9` grid once. For each cell $(r, c)$ with a number:

1. Check if the number exists in the usage set for row `r`.
2. Check if the number exists in the usage set for column `c`.
3. Check if the number exists in the usage set for the sub-box containing $(r, c)$. The sub-box index can be calculated as `(r // 3, c // 3)`.

If any of these conditions are met, duplicates exist, so return `False`.
Otherwise, add the number to the respective valid sets.

## Complexity Analysis

- **Time Complexity:** $O(9^2)$ or $O(1)$ effectively.
  - We iterate over a fixed 81 cells.
- **Space Complexity:** $O(9^2)$ or $O(1)$ effectively.
  - To store the sets for rows, columns, and squares.
