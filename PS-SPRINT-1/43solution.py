def find_all_diivsor(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

print(find_all_diivsor(12))  # [1, 2, 3, 4, 6, 12]