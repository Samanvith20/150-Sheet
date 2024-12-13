try:
    number = int(input("Enter a number: "))  # Convert the input to an integer
    print("Number is:", number)
    if number % 2 == 0:  # Check if the number is divisible by 2
        print("Number is even")
    else:
        print("Number is odd")
except ValueError:
    print("Please enter a valid number.")  # Handle non-numeric input

    
    
    
    
    # IN javascript
#     let input = prompt("Enter a number:");
# let number = parseInt(input);

# if (isNaN(number)) {
#     console.log("Please enter a valid number.");
# } else {
#     console.log("Number is:", number);
#     if (number % 2 === 0) {
#         console.log("Number is even");
#     } else {
#         console.log("Number is odd");
#     }
# }
