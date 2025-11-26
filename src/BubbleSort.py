def BubbleSort(mas):
    for i in range(len(mas)):
        for j in range(0, len(mas) - i - 1):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
    return mas
print(BubbleSort([212, 2, 112, 0, 50]))
