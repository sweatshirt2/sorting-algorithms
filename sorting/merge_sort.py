def mergeSort(nums: list[int]):
    if len(nums) == 1:
        return nums
    l_nums = mergeSort(nums[:len(nums)//2])
    r_nums = mergeSort(nums[len(nums)//2:])
    return merge(l_nums, r_nums)


def merge(l_nums: list[int], r_nums: list[int]):
    l, r, nums = 0, 0, []
    while l < len(l_nums) and r < len(r_nums):
        if l_nums[l] < r_nums[r]:
            nums.append(l_nums[l])
            l += 1
            continue
        nums.append(r_nums[r])
        r += 1
    if l == len(l_nums):
        nums.extend(r_nums[r:])
        return nums
    nums.extend(l_nums[l:])
    return nums