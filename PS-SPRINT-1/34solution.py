# def checkTwoStringAnagram(s1, s2):
#     return sorted(s1) == sorted(s2)

# without using inbulit function
def checkTwoStringAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in s1:
        if i not in s2:
            return False
    return True



print(checkTwoStringAnagram("listen", "silent")) # True