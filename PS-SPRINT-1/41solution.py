def count_occurence_of_digit(n, d):
    count = 0
    while n > 0:
        if n % 10 == d:
            count += 1
        n = n // 10
    return count

# Input and Output
n = int(input("Enter a number: "))
d = int(input("Enter a digit: "))

print(f"Count of {d} in {n}: {count_occurence_of_digit(n, d)}")