def check_perfect_square(n):
    i = 1
    while i * i < n:
        i += 1
    return i * i == n
# using for loop
# def check_perfect_square(n):
#     for i in range(n):
#         if i * i == n:
#             return True

print(check_perfect_square(16))  # True

