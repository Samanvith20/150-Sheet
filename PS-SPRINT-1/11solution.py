# optimal solution
# Function to calculate GCD using the Euclidean Algorithm
def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

# Function to calculate LCM using GCD
def lcm_optimal(a, b):
    return abs(a * b) // gcd(a, b)

# Example Usage
num1 = 12
num2 = 15
print(f"LCM (Optimal) of {num1} and {num2} is: {lcm_optimal(num1, num2)}")

    

# def LCM(a,b):
#     if a > b:
#         greater = a
#     else:
#         greater = b
#     while(True):
#         if((greater % a == 0) and (greater % b == 0)):
#             lcm = greater
#             break
#         greater += 1
#     return lcm


# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# result = LCM(num1,num2)
# print(f"The LCM of {num1} and {num2} is: {result}")