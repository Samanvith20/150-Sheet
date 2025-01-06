def sum_of_primeNumbers_in_Range(start,end):
    sum = 0
    for num in range(start,end+1):
        if num<2:
            continue
        if num > 1:
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    break
            else:
                sum += num
    return sum
    

print(sum_of_primeNumbers_in_Range(1,10)) # 17