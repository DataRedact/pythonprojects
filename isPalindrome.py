def isPalindrome(x):
    numList = list(str(x))
    numList.reverse()
    if numList == list(str(x)):
        return True
    else:
        return False