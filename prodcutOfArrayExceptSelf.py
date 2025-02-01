def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    products = []
    prefixes = []
    suffixes = []
    prefixCurrent = 1
    suffixCurrent = 1
    for numsIndex in range(0, len(nums)):
        prefixCurrent = prefixCurrent*nums[numsIndex]
        prefixes.append(prefixCurrent)
        suffixCurrent = suffixCurrent*nums[len(nums) - 1 - numsIndex]
        suffixes.append(suffixCurrent)
    print(prefixes)
    print(suffixes)
    
    for productsIndex in range(0, len(nums)):
        if productsIndex == 0:
            products.append(suffixes[len(suffixes)-1-productsIndex])
        elif productsIndex == len(nums) - 1:
            products.append(prefixes[productsIndex-1])
        else:
            products.append(prefixes[productsIndex-1]*suffixes[len(suffixes)-2-productsIndex])

    return products
    
print(productExceptSelf([1,2,3,4]))