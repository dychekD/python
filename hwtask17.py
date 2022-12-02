# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

n = int(input('please enter integer n = ' ))
def prime_fac (n: int) -> list:
    prime_factors = []
    temp = [i for i in range (n+1)]
    temp [1] = 0
    for i in range (2, n+1):
        if temp[i] != 0:
            prime_factors.append (temp[i])
            for j in range (i, n+1, i):
                temp[j] = 0
    return prime_factors

result = prime_fac(n)
n_prime_factors = []
for i in range (0, len(result)):
    if n == result [i]:
        print (f'{n} is prime number and can be divided by 1 and inself only')
    elif n % result [i] == 0:
        n_prime_factors.append (result [i])
if n_prime_factors != []:
    print (n_prime_factors)
    