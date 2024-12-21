def sumofList(list):
    sum=0
    # using the range
    # for i in range(len(list)):
    #     sum+=list[i]
    for i in list:
        sum+=i
    return sum

list=[4,7,1,8,5]
print(sumofList(list))