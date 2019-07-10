def two_sum(nums, target):

    length = len(nums)  # get length of array
    for i in range(length):
        for j in range(length):

            value = nums[i] + nums[j]

            if value == target and i != j:
                print([i, j])
                return [nums[i], nums[j]]


print(two_sum([2, 7, 5, 12, 5], 10))
