# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = float(input())
n = abs(n)
n = str(n)
n = n.replace('.','')
n = int(n)
sum = 0
while n >= 1:
    sum = sum + (n % 10)
    n = n // 10
print(f'the sum of digits equals {sum}')




