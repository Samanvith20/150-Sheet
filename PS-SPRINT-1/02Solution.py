try:
    number=int(input("Enter a number:"))
    print("Number is:",number)
    if number%1==0 and number%number==0 and number%2!=0:
        print("Number is prime")
    else:
        print("Number is not prime")
    
except ValueError:
    print("Please enter a valid number.")
    
    # The optimal one
#     def is_prime(num):
#         if num<2:
#             return False
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 return False
#         return True``
# try:
#         num = int(input("Enter a integer number to check if it is a prime number : "))
#      if is_prime(num):
#         print(f"{num} is a prime number....")
#       else:
#         print(f"{num} is not a prime number....")
# except ValueError:
#     print("Invalid input. Please, enter a valid integer number.....")