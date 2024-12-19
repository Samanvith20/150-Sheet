
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
def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
result = GCD(num1,num2)
print(f"The GCD of {num1} and {num2} is: {result}")
    