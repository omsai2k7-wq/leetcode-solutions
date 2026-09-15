def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            return middle

        if nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


# Typical test case
nums = [-1, 0, 3, 5, 9, 12]
target = 9

result = binary_search(nums, target)
print("Typical test case:", result)


# Edge case
nums = [5]
target = 5

result = binary_search(nums, target)
print("Edge case:", result)