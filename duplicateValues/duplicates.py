def duplicates(nums):
    return len(set(nums)) != len(nums)


print(duplicates([1, 2, 3, 4, 3]))
