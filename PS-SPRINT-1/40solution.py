def finding_sum_of_digits(n):
    while n >= 10:  # Continue until n becomes a single digit
        sum_of_digits = 0
        while n > 0:  # Sum the digits of n
            sum_of_digits += n % 10
            n //= 10
        n = sum_of_digits  # Update n to the new sum
    return n  # When n is a single digit, return it

# Input and Output
n = int(input("Enter a number: "))
print(f"Single digit sum: {finding_sum_of_digits(n)}")
