
# def checkPalindrome(num):
#     if num < 0:
#         return False
#     elif num < 10:
#         return True
#     else:
#         num_str = str(num)
#         return num_str == num_str[::-1]
def checkPalindrome(s):
    reversedString = ""
    for i in range(len(s)-1, -1, -1):
        reversedString += s[i]
    return reversedString == s
#Optimal Solution
# def checkPalindrome(s):
#     # Reverse the string using the slicing operator [::-1]
#     return s == s[::-1]

s = input("Enter a string: ")

if checkPalindrome(s):
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")