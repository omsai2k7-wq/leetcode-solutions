# Valid Anagram

Difficulty: Easy

LeetCode: https://leetcode.com/problems/valid-anagram/

## Approach

I used a hash map to count the frequency of each character in the first string.

Then I traversed the second string and decreased the count for each character.

If the lengths are different, the strings cannot be anagrams.

If a character is not present in the hash map, or its count becomes negative, the strings are not anagrams.

If all character counts match, the strings are anagrams.

## Time Complexity

O(n)

The strings are traversed once.

## Space Complexity

O(n)

The hash map stores the frequency of the characters.

## Test Cases

### Typical Test Case

Input:

s = "anagram"

t = "nagaram"

Output:

True

### Edge Case

Input:

s = ""

t = ""

Output:

True

## Notes / Edge Cases

The two strings must have the same length.

Character frequencies must be the same in both strings.

An empty string is considered an anagram of another empty string.

The solution works efficiently using a hash map.
