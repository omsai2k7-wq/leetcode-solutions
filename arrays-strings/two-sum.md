# Two Sum

Difficulty: Easy

LeetCode: https://leetcode.com/problems/two-sum/

## Approach

I used a hash map to store numbers that have already been visited along with their indices.
For every number, I calculated its complement using:

complement = target - number

If the complement already exists in the hash map, the two required indices are returned.

Otherwise, the current number and its index are stored in the hash map.

## Time Complexity

O(n)

The array is traversed once.

## Space Complexity

O(n)

The hash map can store up to n elements.

## Test Cases

### Typical Test Case

Input:

nums = [2, 7, 11, 15]

target = 9

Output:

[0, 1]

### Edge Case

Input:

nums = [3, 3]

target = 6

Output:

[0, 1]

## Notes / Edge Cases

The same element cannot be used twice.

Two different elements may contain the same value.

The solution returns the indices of the two numbers.

Using a hash map avoids checking every possible pair.

## Learning Notes

I learned how a hash map can be used to efficiently find a required complement while traversing an array.
