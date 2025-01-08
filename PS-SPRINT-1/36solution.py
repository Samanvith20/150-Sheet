# def find_NthTriangleNumber(n):
#     return n * (n + 1) // 2
# without using any inbuilt function
def find_NthTriangleNumber(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


print(find_NthTriangleNumber(5))  # 15
