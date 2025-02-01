def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    newS = ''
    for char in s:
        if (ord(char) - 48 >= 0 and ord(char) - 48 <= 9) or (ord(char.lower()) - 97 >= 0 and ord(char.lower()) - 97 <= 25):
            newS = newS + char.lower()
    print(newS)
    i = 0
    j = len(newS) - 1
    isPal = True
    while i <= j:
        if newS[i] != newS[j]:
            isPal = False
            break
        i += 1
        j -= 1
    return isPal

print(isPalindrome("A man, a plan, a canal: Panama"))