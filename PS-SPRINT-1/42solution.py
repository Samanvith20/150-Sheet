def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def generate_fibonacci_sequence(number):
    sequence = []
    for i in range(number):
        sequence.append(fibonacci(i))
    return sequence


number = 9
result = generate_fibonacci_sequence(number)
print(", ".join(map(str, result))) 
