# Min Stack

Difficulty: Medium

LeetCode: https://leetcode.com/problems/min-stack/

## Approach

I used two stacks to implement the Min Stack.

The first stack stores all the values.

The second stack stores the minimum values seen so far.

Whenever a value is pushed, I also add it to the minimum stack if it is smaller than or equal to the current minimum.

When a value is removed, I remove it from the minimum stack if it is the current minimum.

This allows the minimum value to be returned efficiently.

## Time Complexity

O(1)

Push, pop, top, and getMin operations all take constant time.

## Space Complexity

O(n)

The stacks can store up to n elements.

## Test Cases

### Typical Test Case

Operations:

push(-2)

push(0)

push(-3)

getMin()

pop()

top()

getMin()

Output:

-3

0

-2

### Edge Case

Operations:

push(5)

getMin()

Output:

5

## Notes / Edge Cases

The minimum value must be available in constant time.

Duplicate minimum values are handled correctly.

A single-element stack is handled correctly.

The minimum stack keeps track of the smallest value efficiently.

## Learning Notes

I learned how two stacks can be used together to implement a stack that can return the minimum value in constant time.