# 5'. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

from sympy import *
x = symbols('x')
with open ('hwtask20_file1.txt', 'r') as file1:
    data1 = file1.read()
with open ('hwtask20_file2.txt', 'r') as file2:
    data2 = file2.read()
print (data1)
data2 = '+'+data2
print(data2)
result = data1+data2
result = simplify(result)
print (result)
result = str(result)
with open ('hwtask20_file3.txt', 'w') as file3:
    file3.write (result)

