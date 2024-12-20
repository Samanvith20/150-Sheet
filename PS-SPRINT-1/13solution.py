def ReverseaString(s):
    reversedString = ""
    for i in range(len(s)-1, -1, -1):
        reversedString += s[i]
    return reversedString

print(ReverseaString("Hello"))