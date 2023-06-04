def moveZeroes(nums):
    """
    Moves all zeros to the end of the array while maintaining the relative order of non-zero elements.
    """
    n = len(nums)
    left = 0

    # Move non-zero elements to the front of the array
    for i in range(n):
        if nums[i] != 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1

    return nums
