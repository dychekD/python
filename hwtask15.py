# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('enter positive integer ' ))
list_pos = [0, 1, 1]
for i in range (3, n+1):
    list_pos.append (list_pos [i-2]+list_pos[i-1])
list_neg = []
for i in range (0, n):
    list_neg.append(list_pos[len(list_pos)-1-i]*(-1)**(1+(len(list_pos)-1-i)))
print(f'Fibonacci numbers including those with negative indexes for n = {n}')
print(list_neg + list_pos)
