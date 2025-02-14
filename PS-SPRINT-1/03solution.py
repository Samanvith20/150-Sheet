def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

try:
    year = int(input("Enter a year: "))
    print(f"{year} is {'a leap year' if is_leap_year(year) else 'not a leap year'}.")
except ValueError:
    print("Please enter a valid year.")
