def ArmstrongInarange(start, end):
    for i in range(start, end + 1):
        order = len(str(i))
        sum = 0
        temp = i
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if i == sum:
            # Exclude single-digit numbers if needed
            if order > 1:
                print(i)

try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    ArmstrongInarange(start, end)
except ValueError:
    print("Invalid input. Please enter valid integers for start and end.")
