# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('enter integer to convert into binary form: ' ))
result = bin(n)
result = result[2:]
print (f'{n} in binary form: {result}')