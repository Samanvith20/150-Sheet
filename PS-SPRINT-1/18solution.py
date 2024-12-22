def multipicationTable(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num*i}")
try:
    num = int(input("Enter a number: "))
    multipicationTable(num)
except ValueError:
    print("Please enter a valid number.")
    
    
# In Js
# function multipicationTable(num) {
#     for (let i = 1; i <= 10; i++) {
#         console.log(`${num} * ${i} = ${num * i}`);
#     }
# }