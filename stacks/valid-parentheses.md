# Valid Parentheses

Difficulty: Easy

LeetCode: https://leetcode.com/problems/valid-parentheses/

## Approach

I used a stack to check whether the brackets are properly matched.

Opening brackets are pushed onto the stack.

When a closing bracket is found, I check whether it matches the most recent opening bracket.

If it does not match, the string is invalid.

At the end, the stack must be empty for the string to be valid.

## Time Complexity

O(n)

The string is traversed once.

## Space Complexity

O(n)

The stack can store up to n opening brackets.

## Test Cases

### Typical Test Case

Input:

s = "()[]{}"

Output:

True

### Edge Case

Input:

s = ""

Output:

True

## Notes / Edge Cases

Every opening bracket must have a matching closing bracket.

The brackets must be closed in the correct order.

An empty string is considered valid.

The stack helps maintain the correct order of opening brackets.

## Learning Notes

I learned how a stack can be used to match opening and closing brackets efficiently.