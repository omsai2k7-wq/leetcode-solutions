# Binary Search

Difficulty: Easy

LeetCode: https://leetcode.com/problems/binary-search/

## Approach

I used the binary search algorithm to find the target element in the sorted array.

I maintained two pointers: left and right.

I calculated the middle position and compared the middle element with the target.

If the middle element equals the target, I returned its index.

If the middle element is smaller than the target, I searched the right half.

Otherwise, I searched the left half.

If the target was not found, I returned -1.

## Time Complexity

O(log n)

The search space is divided into half after every comparison.

## Space Complexity

O(1)

Only a few variables are used.

## Test Cases

### Typical Test Case

Input:

nums = [-1, 0, 3, 5, 9, 12]

target = 9

Output:

4

### Edge Case

Input:

nums = [5]

target = 5

Output:

0

## Notes / Edge Cases

The input array must be sorted for binary search to work correctly.

If the target is not present, the function returns -1.

A single-element array is handled correctly.
