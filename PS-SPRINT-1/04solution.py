def ArmstrongNumber(number):
    order = len(str(number))
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if number == sum:
        return True
    return False
try:
    number = int(input("Enter a number: "))
    if ArmstrongNumber(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
except ValueError:
    print("Please enter a valid number.")