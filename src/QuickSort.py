def QuickSort(mas, l, r):
    i = l
    j = r
    middle = (l + r) // 2
    while (i <= j):
        while (mas[i] < mas[middle] and i < r):
            i += 1
        while (mas[j] > mas[middle] and j > l):
            j -= 1
        if (i <= j):
            mas[i], mas[j] = mas[j], mas[i]
            i += 1
            j -= 1
    if (l < j):
        QuickSort(mas, l, j)
    if (i < r):
        QuickSort(mas, i, r)
    return mas
print(QuickSort([212, 2, 112, 0, 50], 0, 4))

    
