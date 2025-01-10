# def length_of_string_(s):
#     return len(s)

# without using any inbuilt functions
def length_of_string(s):
    count = 0
    for i in s:
        count += 1
    return count


# Test the function with a sample input
s = "hello"
print(length_of_string(s))  # Output: 5