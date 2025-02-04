def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # create dictionary to mimic hash logic, all entries already given will be overwritten
    myHash = {}
    # loop through list and add to dictionary, overwrite duplicate entrys
    for index in range(0, len(nums)):
        myHash[nums[index]] = index
    # if len(myHash) is shorted than len(nums), return true, else false
    return len(myHash) < len(nums)
    # this could have been done more efficiently using python's set() function

print(containsDuplicate([-1,1,3,4,5,8,-1]))