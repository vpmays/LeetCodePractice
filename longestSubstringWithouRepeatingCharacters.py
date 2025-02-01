def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    newSubString = ''
    longestSubstring = 0
    for sIndex in range(0, len(s)):
        if s[sIndex] in newSubString:
            if len(newSubString) > longestSubstring:
                longestSubstring = len(newSubString)
            newSubString = newSubString[newSubString.find(s[sIndex])+1:]
        newSubString = newSubString + s[sIndex]
    if len(newSubString) > longestSubstring:
        return len(newSubString)
    else:
        return longestSubstring
print(lengthOfLongestSubstring('abcdefghijklmnopqrstuvwxyazj'))