def cycleSort(nums: list[int]):
    i, count = 0, 0
    while (i < len(nums) - 1):
        current = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] < current:
                count += 1
        if count == 0:
            i += 1
            continue
        temp = nums[count + i]
        nums[count + i] = current
        nums[i] = temp
        count = 0
    return nums