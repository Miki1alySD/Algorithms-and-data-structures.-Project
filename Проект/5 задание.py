#Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50]. 
#Выведите на экран исходный и отсортированный массивы.

import random

n = 10
arr = [random.randint(0, 50) for i in range(n)]
print("Не отсортированный: ")
print(arr)
print("----------")


def merge_sort(a):
    if len(a) < 2:
        return a
    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:len(a)])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        a[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        a[k] = right[j]
        j = j + 1
        k = k + 1
    return a

print("Отсортированный: ")
print(merge_sort(arr))