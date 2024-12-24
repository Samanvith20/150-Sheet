# A perfect number is a positive integer that is equal to the sum of its positive proper divisors, excluding the number itself

def PerfectNumber(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
    
try:
    num = int(input("Enter a number: "))
    if PerfectNumber(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
except ValueError:
    print("Please enter a valid number.")