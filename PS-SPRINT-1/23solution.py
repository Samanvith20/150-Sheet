def fibonnacinumberatnthpostion(n):
    list = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        list.append(0)
        list.append(1)
        for i in range(2, n + 1):
            list.append(list[i - 1] + list[i - 2])
        return list[n]
try:
    print(fibonnacinumberatnthpostion(int(input("Enter the postion: "))))
except ValueError:
    print("Invalid input. Please enter a valid number.")