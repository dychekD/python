# squared number

# a = int(input())   # input is always text
# print(a**2)

# two numbers, if one is squared of the other

# a = int(input())
# b = int(input())
# if a == b**2 or b == a**2:
#     print(f'{a} is squared {b}')
# elif b == a**2:
#     print(f'{b} is squared {a}')
# else:
#     print(f'{a} is not squared {b}')

# print((a == b**2) or (b == a**2))

# 5 numbers, finds max

# max = int(input())
# for i in range(4):
#     b = int(input())
#     if b > max:
#         max = b
# print(max)

# a = list(map(int, input().split()))
# print(max(a))

# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# n = int(input())
# a = [-n]
# for i in range(-n+1, n+1):
#     a.append(i)
# print(a)


# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# n = float(input())
# b = int(n)
# res = int((n - b)*10)
# print(res)


# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

n = int(input())
if n % 5 == 0 and n % 10 == 0 or n % 15 == 0:
    if n % 30 != 0:
        print ('yes')
    else:
        print ('no')
else:
    print ('no')