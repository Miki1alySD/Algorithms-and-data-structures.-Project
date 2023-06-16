# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100]. 
#Выведите на экран исходный и отсортированный массивы. 
#Примечания: 
#a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных; 
#b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. 
#Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

def bubble_sort(lst):
    n = 1
    while n < len(lst):
        count = 0
        for i in range(len(lst) - 1 - (n - 1)):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1
        if count == 0:
            break
        n += 1

SIZE = 40
MIN_ITEM = -100
MAX_ITEM = 99
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Массив:', arr, sep='\n')
print("-----------")
bubble_sort(arr)
print('После сортировки:', arr, sep='\n')