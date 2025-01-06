def FindMedian(list):
    list.sort()
    n = len(list)
    if n % 2 == 0:
        return (list[n // 2 - 1] + list[n // 2]) / 2
    else:
        return list[n // 2]

list = [3, 1, 2, 4, 5]
print(FindMedian(list))  # 3