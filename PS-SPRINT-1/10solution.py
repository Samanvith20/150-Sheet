
# Brute force solution
# def GCD(a,b):
#     # need to find which is smallest number
#     if a < b:
#         smaller = a
#     else:
#         smaller = b
#     for i in range(1, smaller+1):
#         if((a % i == 0) and (b % i == 0)):
#             gcd = i
#     return gcd

# Optimized solution
def GCD(a, b):
    while b != 0:  # Continue the loop as long as b is not zero
        remainder = a % b  # Calculate the remainder when a is divided by b
        a = b  # Update a to the value of b
        b = remainder  # Update b to the remainder
    return a  # When b becomes zero, a is the GCD


num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
result = GCD(num1,num2)
print(f"The GCD of {num1} and {num2} is: {result}")
    