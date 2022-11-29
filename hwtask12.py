# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 
import math
list_initial = list(map(int, input('enter list of integers separated by space: ').split()))
list_result = [list_initial[i]*list_initial[len(list_initial)-1-i] for i in range (0, math.ceil(len(list_initial)/2))]
print (list_result)