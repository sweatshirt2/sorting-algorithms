def countSort(nums: list[int]):
    sorted = [0] * len(nums)
    minimum = min(nums)
    maximum = max(nums)
    orders = [0] * (maximum - minimum + 1)
    for num in nums:
        orders[num - minimum] += 1
    for i in range(1, len(orders)):
        orders[i] += orders[i - 1]
    start = maximum
    for i in range(len(orders) - 1, 0, -1):
        k = orders[i]
        while (k > orders[i - 1]):
            sorted[k - 1] = start
            k -= 1
        start -= 1
    return sorted