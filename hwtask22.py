# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму

n = int(input())
#v1
res = []
for i in range (1, n+1):
    res.append ((1+1/i)**i)
print (res)
print (sum(res))

#v2
res1 = [(1+1/i)**i for i in range (1, n+1)]
print (res1)
print (sum(res1))