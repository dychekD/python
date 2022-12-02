# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
n = int(input ('please enter the size of the initial array: ' ))
list1 = [random.randint (0, 10) for i in range (n+1)]
print (list1)
list2 = set(list1)
print (list2)
