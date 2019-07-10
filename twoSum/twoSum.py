def two_sum(nums, target):

    lenght = len(nums)

    for i in range(lenght):
        for j in range(lenght):
            value = nums[i] + nums[j]

            if value == target and i != j:
                return print(' number ' + str(nums[i]) +
                             ' number ' + str(nums[j]) + ' = ' + str(target))


print(two_sum([4, 7, 15, 12, 5], 9))
