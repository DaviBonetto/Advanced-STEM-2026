# Valid Palindrome

## Problem

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Solution Approach: Two Pointers

1. Initialize two pointers: `l` (left) at 0 and `r` (right) at `len(s) - 1`.
2. While `l < r`:
   - Move `l` forward if `s[l]` is not alphanumeric.
   - Move `r` backward if `s[r]` is not alphanumeric.
   - Compare `s[l].lower()` and `s[r].lower()`.
   - If they are different, return `False`.
   - Otherwise, `l += 1` and `r -= 1`.

This avoids creating a new filtered string, keeping space complexity minimal.

## Complexity Analysis

- **Time Complexity:** $O(n)$
  - We traverse the string once with two pointers meeting in the middle.
- **Space Complexity:** $O(1)$
  - No extra string or array is created, just constant interactions.
