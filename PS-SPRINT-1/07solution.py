
# # But in this approach we are iterating through  each number from 1 to height
# def printPattern(pattern,height):
#     if pattern=="pyramid":
#                 # Pyramid pattern
#         for i in range(1, height + 1):
#             spaces = " " * (height - i)
#             stars = "*" * (2 * i - 1)
#             print(spaces + stars)
# we can optimize this by using the below approach
def pyramid_pattern(height):
    for i in range(1, height * 2, 2):  # Loop for odd numbers: 1, 3, 5, ...
        spaces = " " * ((height * 2 - 1 - i) // 2)  # Calculate spaces
        stars = "*" * i  # Calculate stars
        print(spaces + stars)


# pattern=input("Enter the pattern   : ")
height=int(input("Enter the height of the pattern: "))
# printPattern(pattern,height)
pyramid_pattern(height)