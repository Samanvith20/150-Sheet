# def findingDigitsinNumber(num):
#     count = 0
#     while num > 0:
#         num //= 10
#         count += 1
#     return count

# def findingDigitsinString(str):
#     count = 0
#     for i in str:
#         count += 1
#     return count
def bothstringandnumber(input_string):
    count = 0
    for i in input_string:
        count += 1
    return count

input=input("Enter a string or number:")
print(bothstringandnumber(input))