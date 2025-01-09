def square_matrix_of_size(n):
    if n <= 0:
        return []  # Return an empty list for invalid sizes
    count = 1
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(count)
            count += 1
        matrix.append(row)
    return matrix




print(square_matrix_of_size(4))