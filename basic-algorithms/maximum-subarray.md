# Maximum Subarray

Difficulty: Medium

LeetCode: https://leetcode.com/problems/maximum-subarray/

## Approach

I used Kadane's algorithm to find the maximum sum of a contiguous subarray.

I maintained two variables: current_sum and max_sum.

current_sum stores the maximum subarray sum ending at the current position.

For each number, I decided whether to start a new subarray or continue the existing subarray.

max_sum stores the maximum sum found so far.

## Time Complexity

O(n)

The array is traversed once.

## Space Complexity

O(1)

Only a few variables are used.

## Test Cases

### Typical Test Case

Input:

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output:

6

### Edge Case

Input:

nums = [-5]

Output:

-5

## Notes / Edge Cases

The subarray must contain at least one element.

The array may contain negative numbers.

A single-element array is handled correctly.

Kadane's algorithm provides an efficient solution without using extra space.

## Learning Notes

I learned how Kadane's algorithm can be used to find the maximum sum of a contiguous subarray efficiently.