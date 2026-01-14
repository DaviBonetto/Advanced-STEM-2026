# Product of Array Except Self

## Problem

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. All entries fit in a 32-bit integer.

**Constraint:** You must write an algorithm that runs in $O(n)$ time and without using the division operation.

## Solution Approach: Prefix and Postfix Products

Since we cannot use division, we calculate the product of all elements to the **left** of `i` and all elements to the **right** of `i`.

`answer[i] = prefix[i] * postfix[i]`

To do this in $O(1)$ extra space (excluding the output array):

1. **First Pass (Left -> Right):** Calculate prefix products. Store them directly in the result array `res`.
   - `res[i]` will hold the product of `nums[0]...nums[i-1]`.
2. **Second Pass (Right -> Left):** Maintain a running `postfix` product variable.
   - Multiply `res[i]` by the current `postfix`.
   - Update `postfix` by multiplying it with `nums[i]`.

## Complexity Analysis

- **Time Complexity:** $O(n)$
  - Two passes over the array.
- **Space Complexity:** $O(1)$
  - We only use the output array `res` and a variable `postfix`. The problem statement says the output array doesn't count as extra space.
