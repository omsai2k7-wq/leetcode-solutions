def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Typical test case
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = max_subarray(nums)
print("Typical test case:", result)


# Edge case
nums = [-5]

result = max_subarray(nums)
print("Edge case:", result)