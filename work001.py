"""
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""



def Progression(first_number: int, length: int, difference: int):
    result = [first_number]
    for i in range(length-1):
        first_number += difference
        result.append(first_number)
    return result

first_number = int(input('Введите первый элемент прогрессии: '))
length = int(input('Введите количество элементов прогрессии: '))
difference = int(input('Введите разность соседних элементов: '))
print(Progression(first_number,length,difference))