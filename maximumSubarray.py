def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #maxSumSubarray = nums[0:1]
    
    currentSum = nums[0]
    currentAns = nums[0]
    for numsIndex in range(1, len(nums)):
        print(f"current num: {nums[numsIndex]}")
        if currentSum > 0:
            currentSum += nums[numsIndex]
        else:
            currentSum = nums[numsIndex]
        print(f"currentSum: {currentSum}")
        if currentSum > currentAns:
            currentAns = currentSum
        print(f"currentAns: {currentAns}")

    return currentAns

print(maxSubArray([1,4,-3,4]))