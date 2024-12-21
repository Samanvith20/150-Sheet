def findlargestandsmalest(list):
    largest=list[0]
    smallest=list[0]
    # run a loop using a for loop
    for i in list:
        if i>largest:
            largest=i
        elif i<smallest:
            smallest=i
    # for i in range(1,len(list)):
    #     if list[i]>largest:
    #         largest=list[i]
    #     elif list[i]<smallest:
    #         smallest=list[i]
    return largest,smallest

list=[4,7,1,8,5]
largest,smallest=findlargestandsmalest(list)
print("Largest number:",largest)
print("Smallest number:",smallest)