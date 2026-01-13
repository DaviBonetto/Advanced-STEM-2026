# Contains Duplicate

## Problem

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Solution Approach: Hash Set

We can use a Hash Set to check for duplicates efficiently. A Hash Set gives us $O(1)$ average time complexity for insertion and search.

We iterate through the array `nums`. For each element `n`:

- Check if `n` is already in the `hashset`.
- If it is, we found a duplicate, return `True`.
- If not, add `n` to the `hashset`.

If the loop finishes without finding duplicates, return `False`.

## Complexity Analysis

- **Time Complexity:** $O(n)$

  - We do `search()` and `insert()` for $n$ times and each operation takes constant time.

- **Space Complexity:** $O(n)$
  - The space used by a hash table is linear with the number of elements in it.
