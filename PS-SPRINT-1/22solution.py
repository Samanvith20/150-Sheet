def sumofOddNumbers(start, end):
    sum = 0
    for i in range(start, end+1):
        if i % 2 != 0:
            sum += i
    return sum

try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    result = sumofOddNumbers(start, end)
    print(f"The sum of odd numbers in the range {start} to {end} is: {result}")
except ValueError:
    print("Invalid input. Please enter valid integers for start and end.")