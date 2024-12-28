def findMissingnumber(arr):
    n = len(arr)
    total = (n+1)*(n+2)/2
    sum_of_arr = sum(arr)
    return total - sum_of_arr

arr = [1, 2, 4, 5, 6]
result = findMissingnumber(arr)
print(f"The missing number in the array is: {int(result)}")


def find_missing_numbers(sequence, n):
    # Create a list for the full sequence from 1 to n
    full_sequence = []
    for i in range(1, n + 1):
        full_sequence.append(i)
    
    # Remove duplicates from the given sequence
    unique_sequence = []
    for num in sequence:
        if num not in unique_sequence:
            unique_sequence.append(num)
    
    # Find missing numbers
    missing_numbers = []
    for num in full_sequence:
        if num not in unique_sequence:
            missing_numbers.append(num)
    
    return missing_numbers

# Input
sequence = [1, 2, 2, 3]
n = 4

# Find and print missing numbers
result = find_missing_numbers(sequence, n)
print(f"The missing numbers are: {result}")
