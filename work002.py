"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

def InTheList(list_1: list, max: int, min: int, result = [], count = 0):
    for i in list_1:
        if i <= max and i >= min:
            result.append(numbers.index(i,count))
            count += 1
    return result


numbers = [1, 8, 5, 2, 6, 7, 9, 8, 3, 4]
max = 10
min = 6

print(InTheList(numbers, max, min))