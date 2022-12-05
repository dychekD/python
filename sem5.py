# 1 Задано N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# *' 1 2 3 4 6 7 -> 5
# *' 1 3 -> 2

# mass = "1 3"
# mass = list(map(int, mass.split()))
# for i in range(1, len(mass)):
#     if mass[i] - 1 != mass[i-1]:
#         print(i+1)

# 2 Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

mass = [1, 5, 2, 3, 4, 6, 1, 7]
new_mass = []
b = 0
for i in range(0, len(mass)-1):
    if mass[i] != max(mass):
        new_mass.append(mass[i])
        b = i
        break
for i in range(b+1, len(mass)):
    if mass[i] > new_mass[len(new_mass) - 1]:
        new_mass.append(mass[i])
print(new_mass)


# 3 Напишите программу, удаляющую из текста все слова, содержащие "абв".
# *' 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

# txt = 'абвгд гдежз жзе абв ыопыпт'
# iskom_txt = "абв"
# stroka = [i for i in txt.split() if iskom_txt not in i]
# print(f'Результат: {" ".join(stroka)}')
