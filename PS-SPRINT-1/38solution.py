# def sum_of_squares_of_digits(n):
#     return sum([int(i)**2 for i in str(n)])
# In a simple way
# def sum_of_squares_of_digits(n):
#     sum = 0
#     for i in str(n):
#         sum += int(i)**2
#     return sum


def sum_of_squares_of_digits(number):
    # Ensure the number is positive
    number = abs(number)
    sum_of_squares = 0
    
    while number > 0:
        digit = number % 10  # Get the last digit
        sum_of_squares += digit ** 2  # Add the square of the digit
        number //= 10  # Remove the last digit from the number
    
    return sum_of_squares

print(sum_of_squares_of_digits(123))