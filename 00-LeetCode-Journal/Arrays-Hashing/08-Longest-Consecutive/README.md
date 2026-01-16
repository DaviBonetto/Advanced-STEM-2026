# Longest Consecutive Sequence

## Problem

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

**Constraint:** You must write an algorithm that runs in $O(n)$ time.

## Solution Approach: Hash Set (Start of Sequence)

We can process this in linear time by observing that we only need to count a sequence if we are at the **start** of that sequence.

1. Convert `nums` to a Set called `numSet` for $O(1)$ lookups.
2. Iterate through each number `n` in `nums`.
3. Check if `n - 1` exists in `numSet`.
   - If it **does exist**, then `n` is NOT the start of a sequence (the sequence would have started at `n-1` or earlier). We skip it.
   - If it **does not exist**, then `n` IS the start of a sequence. We enter a while loop checking `n+1`, `n+2`, ... until the sequence breaks.
4. Record the max length found.

## Complexity Analysis

- **Time Complexity:** $O(n)$
  - Although there is a nested loop, the `while` loop only runs for the start of sequences. Each number is visited essentially once by the inner logic. Complexity is strictly linear.
- **Space Complexity:** $O(n)$
  - To store the `numSet`.
