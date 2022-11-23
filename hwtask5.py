# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math
x1 = float(input('enter x coordinate of the first dot '))
y1 = float(input('enter y coordinate of the first dot '))
x2 = float(input('enter x coordinate of the second dot '))
y2 = float(input('enter y coordinate of the second dot '))
res = round(math.sqrt((x2-x1)**2 + (y2 - y1)**2), 2)
print(f'the distance between dots with coordinates ({x1}; {y1}) and ({x2}; {y2}) equals {res}')
