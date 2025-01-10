def number_pyramid(rows):
    for i in range(1, rows + 1):
        # Print numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end="")  # Print numbers on the same line
        print()  # Move to the next line after each row

# Example usage
rows = 4
number_pyramid(rows)
