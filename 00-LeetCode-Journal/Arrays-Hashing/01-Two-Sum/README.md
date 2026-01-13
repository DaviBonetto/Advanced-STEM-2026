# Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Solution Approach: Hash Map (Dictionary)

We can solve this problem efficiently by using a Hash Map to store the values we have encountered so far and their indices.

As we iterate through the array, for each number `n`, we calculate its complement `diff = target - n`. We then check if `diff` exists in our Hash Map.

- If it does, we have found the pair! We return the index stored in the map for `diff` and the current index `i`.
- If not, we add the current number `n` and its index `i` to the map and continue.

## Complexity Analysis

- **Time Complexity:** $O(n)$

  - We traverse the list containing $n$ elements only once. Each look up in the hash table costs only $O(1)$ time on average.

- **Space Complexity:** $O(n)$
  - The extra space required depends on the number of items stored in the hash table, which stores at most $n$ elements.
