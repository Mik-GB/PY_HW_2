# Задача 12: Петя и Катя – брат и сестра. Петя – студент, 
# а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две 
# подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# Пример:
# Ввод: 5 6 -> 2 3

sum = int(input('Введите сумму чисел: '))
prod = int(input('Введите произведение чисел: '))
flag = True
for x in range(sum):
    if x * (sum - x) == prod:
        print(f'число X = {x}, число Y = {sum - x}')
        flag = False
        break
if flag:
        print('Неверные числа')