def generate_pascals_triangle(num_rows):
    # Initialize the triangle with an empty list
    triangle = []

    for row_num in range(num_rows):
        # Start each row with 1
        row = [1]
        
        # Fill the middle values of the row
        if triangle:  # Check if there are previous rows
            last_row = triangle[-1]  # Get the previous row
            for i in range(len(last_row) - 1):
                # Compute the next element by summing adjacent values in the previous row
                row.append(last_row[i] + last_row[i + 1])
            # End the row with 1
            row.append(1)

        # Add the row to the triangle
        triangle.append(row)

    return triangle

# Print Pascal's Triangle for 5 rows
num_rows = 5
triangle = generate_pascals_triangle(num_rows)
for row in triangle:
    print(row)
