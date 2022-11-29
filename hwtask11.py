# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_for_odd = list(map(int, input('enter list of integers separated by space: ').split()))
sum = 0
for i in range (1, len(list_for_odd)-1, 2):
    sum += list_for_odd [i]
print (f'sum of elements with odd indexes equals {sum}')