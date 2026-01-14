# Group Anagrams

## Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

## Solution Approach: Character Count Tuple

Two strings are anagrams if and only if their character counts (how many times each character appears) are the same.

Instead of sorting each string (which would be $O(m \cdot n \log n)$), we can count the frequency of each character.
Since there are 26 lowercase English letters, we can use an array of size 26 as the key for our Hash Map.

1. Create a dictionary (Hash Map) where the key is the character count tuple and the value is the list of strings.
2. Iterate through each string `s` in `strs`.
3. Count the characters in `s` to create a count array/tuple (e.g., `(1, 0, 2, ...)` representing 1 'a', 0 'b', 2 'c'...).
4. Use this tuple as the key in the map and append `s` to the listing.

## Complexity Analysis

- **Time Complexity:** $O(m \cdot n)$

  - where $m$ is the number of strings and $n$ is the average length of a string. We iterate through each string once and count its characters.

- **Space Complexity:** $O(m \cdot n)$
  - To store the hash map and the output groups.
