
def summarizing_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

num = int(input("Enter a number: "))
result = summarizing_digits(num)
print(f"The sum of the digits of {num} is: {result}")