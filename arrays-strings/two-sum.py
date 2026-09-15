def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []


# Typical test case
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print("Typical test case:", result)


# Edge case
nums = [3, 3]
target = 6

result = two_sum(nums, target)
print("Edge case:", result)