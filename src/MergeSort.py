def merge(left, right):
    mas = []
    N = len(left)
    M = len(right)
    i = 0
    j = 0
    
    while i < N and j < M:
        if left[i] <= right[j]:
            mas.append(left[i])
            i += 1
        else:
            mas.append(right[j])
            j += 1

    mas += left[i:] + right[j:]

    return mas

def MergeSort(mas):
    middle = len(mas) // 2 
    left = mas[:middle]
    right = mas[middle:]

    if len(left) > 1:
        left = MergeSort(left)

    if len(right) > 1:
        right = MergeSort(right)

    return merge(left, right)

