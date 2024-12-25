import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False
    return True

def print_prime_numbers(start, end):
    """Print all prime numbers in the given range."""
    if start > end:
        print("Start number must be less than or equal to end number.")
        return

    # Ensure start is at least 2
    start = max(start, 2)
    
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    
    if primes:
        print("Prime numbers between {} and {}:".format(start, end))
        print(" ".join(map(str, primes)))
    else:
        print("No prime numbers found in the given range.")

def main():
    try:
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))
        print_prime_numbers(start, end)
    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
