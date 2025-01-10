def find_average_of_numbers_in_list(numbers):
    total = 0
    for i in numbers:
        total += i
    return total / len(numbers)


result = find_average_of_numbers_in_list([1, 2, 3, 4, 5])
print(result)  
