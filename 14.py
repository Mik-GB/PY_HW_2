# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.

# Пример:
# Ввод: 13 -> 1, 2, 4, 8

number = abs(int(input('Введите число: ')))
x = 0
length = number // 2
for x in range(length):
    if 2 ** x <= number:
        print(2 ** x)
        x += 1
