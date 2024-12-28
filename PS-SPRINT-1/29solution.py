def find_Palindrome(str):
    return str==str[::-1]

def  largest_palindrome(str):
    max_length=0
    largest_Palindrome=""
    n=len(str)
    for i in range(n):
        for j in range(i,n):
            substring=str[i:j+1]
            if find_Palindrome(substring) and len(substring)>max_length:
                max_length=len(substring)
                largest_Palindrome=substring
    return largest_Palindrome
              
        

str = input("Enter a string: ")
result = largest_palindrome(str)
print(f"The largest palindrome in the string is: {result}")