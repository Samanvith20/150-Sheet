def sort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
    return list

         
 
list=[4,7,1,8,5]
print(sort(list))           