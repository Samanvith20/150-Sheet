def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_series = [0, 1]  # Initialize the series with the first two terms
    for i in range(2, n):  # Start from the third term
        next_term = fib_series[-1] + fib_series[-2]  # Sum of the last two terms
        fib_series.append(next_term)  # Add the new term to the series
    return fib_series

# Example Usage
num_terms = int(input("Enter the number of terms: "))
result = fibonacci_series(num_terms)
print(f"Fibonacci Series up to {num_terms} terms: {result}")
