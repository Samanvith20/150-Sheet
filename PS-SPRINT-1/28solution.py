def sum_of_digits_of_factorial(n):
    # Calculate factorial of n
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Calculate the sum of the digits of the factorial
    digit_sum = 0
    for digit in str(factorial):
        digit_sum += int(digit)

    return digit_sum

# Input from the user
number = int(input("Enter a number: "))
result = sum_of_digits_of_factorial(number)
print(f"The sum of the digits of the factorial of {number} is {result}.")
