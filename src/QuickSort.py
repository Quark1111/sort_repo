def QuickSort(mas, l, r):
    if l < r:
        i = l
        j = r
        middle = (l + r) // 2
        privot = mas[middle]
        while (i <= j):
            while (mas[i] < privot):
                i += 1
            while (mas[j] > privot):
                j -= 1
            if (i <= j):
                mas[i], mas[j] = mas[j], mas[i]
                i += 1
                j -= 1
        if (l <= j):
            QuickSort(mas, l, j)
        if (i < r):
            QuickSort(mas, i, r)
    return mas
