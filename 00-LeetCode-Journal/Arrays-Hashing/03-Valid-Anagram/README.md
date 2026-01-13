# Valid Anagram

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

## Solution Approach: Frequency Counter (Hash Map)

An anagram is produced by rearranging the letters of a string. Therefore, if `t` is an anagram of `s`, they must have the same length and the same characters with the same frequencies.

1. First, check if `len(s)` is equal to `len(t)`. If not, return `False`.
2. Use two hash maps (dictionaries) to count the occurrences of each character in `s` and `t`.
3. Iterate through the strings and update the counts.
4. Compare the two maps. If they are equal, return `True`.

Alternatively, we could sort the strings and compare them, but that would be $O(n \log n)$. This frequency count method is faster.

## Complexity Analysis

- **Time Complexity:** $O(n)$

  - We iterate through the strings once to build the counts, which is $O(n)$. Comparing the maps is close to $O(1)$ since there are at most 26 lowercase English letters (or slightly more for full Unicode, but bounded).

- **Space Complexity:** $O(1)$ (or $O(n)$ generically)
  - Since the problem usually implies input consists of lowercase English letters, the table size is constant (26). In a generic case, it's $O(n)$.
