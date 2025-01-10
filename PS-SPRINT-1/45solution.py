def mode_in_a_list(numbers):
    mode = 0
    max_count = 0
    for i in numbers:
        count = numbers.count(i)
        if count > max_count:
            max_count = count
            mode = i
    return mode

result = mode_in_a_list([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1])
print(result)

def find_mode(array):
    # Dictionary to store the frequency of each number
    frequency = {}
    
    # Count how many times each number appears in the array
    for number in array:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    # Find the number with the highest frequency
    max_frequency = max(frequency.values())
    mode = [key for key, value in frequency.items() if value == max_frequency]

    # If there is only one mode, return it; otherwise, return all modes
    return mode[0] if len(mode) == 1 else mode

# Example usage
array = [1, 2, 2, 3, 4, 4, 4]
result = find_mode(array)
print(result)  # Output: 4
