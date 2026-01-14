# Top K Frequent Elements

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## Solution Approach: Bucket Sort

A naive solution would count frequencies and then sort the map by value, which takes $O(n \log n)$. We can improve this to $O(n)$.

1. Use a Hash Map `count` to find the frequency of each element.
2. Use **Bucket Sort**: Create an array `freq` where the index represents the frequency, and the value is a list of numbers that have that frequency.
   - The size of `freq` will be `len(nums) + 1` (a number can appear at most `n` times).
3. Populate the buckets.
4. Iterate through the `freq` array from the **end** (highest frequency) to the beginning.
5. Add numbers to our result list until we reach `k` elements.

## Complexity Analysis

- **Time Complexity:** $O(n)$
  - Counting frequencies takes $O(n)$. Bucketing takes $O(n)$. Iterating buckets takes $O(n)$.
- **Space Complexity:** $O(n)$
  - To store the `count` map and the `freq` buckets.
