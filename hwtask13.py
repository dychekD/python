# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_initial = list(map(float, input('enter list of double numbers separated by space: ').split()))
list2 = []
for i in range (0, len(list_initial)):
    list2.append(str(list_initial[i]))
list3 = []
res = ''
for item in list2:
    for g in range (0, len(item)):
        if g > item.find('.'):
            res += item [g]          
    list3.append (res)
    res = ''
max_len = 0
for item in list3:
    if len(item) > max_len:
        max_len = len(item)
list4 = []
for item in list3:
    if len (item) == max_len:
        list4.append(item)
    elif len (item) < max_len:
        list4.append(item + ((max_len - len(item))*'0'))
list5 = [int(i) for i in list4]
list6 = []
for i in list5:
    if i !=0:
        list6.append(i)
print (f'the difference between max and min fractional parts in the list equals: {(max(list6) - min(list6)) / 10**max_len}')

