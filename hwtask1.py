# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input())
if day == 6 or day == 7:
    print ('yes')
else:
    print('no')