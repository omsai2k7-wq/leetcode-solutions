# Merge Two Sorted Lists

Difficulty: Easy

LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/

## Approach

I used an iterative approach to merge the two sorted linked lists.

I created a dummy node to simplify the merging process.

I compared the values of the current nodes from both lists.

The smaller value was connected to the merged list, and the pointer was moved forward.

After one list was completely processed, I connected the remaining nodes from the other list.

Finally, I returned the node after the dummy node as the head of the merged list.

## Time Complexity

O(n + m)

Each node from both linked lists is visited once.

## Space Complexity

O(1)

Only a few pointer variables are used.

## Test Cases

### Typical Test Case

Input:

list1 = [1, 2, 4]

list2 = [1, 3, 4]

Output:

[1, 1, 2, 3, 4, 4]

### Edge Case

Input:

list1 = []

list2 = [0]

Output:

[0]

## Notes / Edge Cases

One or both input lists can be empty.

The input lists are already sorted.

All nodes are reused instead of creating a new list of values.

The iterative approach uses constant extra space.

## Learning Notes

I learned how to merge two sorted linked lists by comparing nodes and adjusting their next pointers efficiently.
