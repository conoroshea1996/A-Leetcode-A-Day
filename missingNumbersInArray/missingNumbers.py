def missingNumbers(arr):
    nums = set(arr)

    missing = []

    for num in range(0, len(arr)+1):
        if num not in nums:
            missing.append(num)

    return missing


print(missingNumbers([1, 2, 8, 3, 4, 5, 3, 3]))
