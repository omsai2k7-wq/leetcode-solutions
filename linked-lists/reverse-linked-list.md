# Reverse Linked List

Difficulty: Easy

LeetCode: https://leetcode.com/problems/reverse-linked-list/

## Approach

I used an iterative approach to reverse the linked list.

I maintained three references: previous, current, and next_node.

For each node, I stored the next node before changing the current node's next pointer.

Then I changed the current node's next pointer to point to the previous node.

Finally, I moved the previous and current references forward.

When all nodes were processed, previous became the new head of the reversed linked list.

## Time Complexity

O(n)

Each node is visited once.

## Space Complexity

O(1)

Only a few pointer variables are used.

## Test Cases

### Typical Test Case

Input:

head = [1, 2, 3, 4, 5]

Output:

[5, 4, 3, 2, 1]

### Edge Case

Input:

head = []

Output:

[]

## Notes / Edge Cases

An empty linked list returns an empty list.

A single-node linked list remains unchanged.

The original links are reversed by changing the next pointers.

The iterative solution uses constant extra space.

## Learning Notes

I learned how to reverse a linked list by changing the direction of each node's next pointer using an iterative approach.
