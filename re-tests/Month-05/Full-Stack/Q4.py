def getSubstr(s):

    res, temp = 1, 1
    for i in range(1, len(s)):
        if (s[i] == s[i - 1]):
            temp += 1
        else:
            res = max(res, temp)
            temp = 1
    res = max(res, temp)
    return res

s = "attcggga"
print(getSubstr(s))