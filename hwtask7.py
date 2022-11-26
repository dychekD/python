# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input())
res = [1]
for i in range(1,n):
    res.append(res [i-1] * (i+1))
print(res)
