def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_prime_factors(number):
    prime_factors_sum = 0
    # Check for divisibility by all numbers up to the square root of the number
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            prime_factors_sum += i
    return prime_factors_sum

# Example usage
number = 12
result = sum_of_prime_factors(number)
print(result)  # Output: 5
