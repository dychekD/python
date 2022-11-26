# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) 
# -2 -1 0 1 2 Позиции: 0,1 -> 2

n = int(input('enter positive integer ' ))
list_n = []
for i in range (n * 2 + 1):
    list_n.append (-n+i)
print (list_n)

infile = open('positions.txt')
list_positions = []
for item in infile:
    list_positions.append (int(item))
print (f'{list_positions} - list of indexes from file positions.txt')
infile.close()

product = 1
for i in list_positions:
    product = product * list_n[i]
print (f'product of numbers with indexes from file positions.txt equals {product}')


