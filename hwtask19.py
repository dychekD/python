# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 
import random
k = int(input('enter the natural degree for the equation: ' ))
multiplier = [random.randint(0, 100) for i in range (k+1)]
print (multiplier)
result = ''
if multiplier [0] == 1:
    result = f'x**{k}'
elif multiplier [0] != 0:
    result = f'{multiplier [0]}*x**{k}'
for i in range (1, len(multiplier)-1):
    if multiplier [i] == 0:
        result += ''
    elif multiplier [i] == 1:
        result += f'+x**{len(multiplier)-1-i}'
    else:
        result += f'+{multiplier [i]}*x**{len(multiplier)-1-i}'
# if multiplier [len(multiplier)-2] !=0:
#     result += f'+{multiplier [len(multiplier)-2]}*x'
if multiplier [len(multiplier)-1] != 0:
    result += f'+{multiplier [len(multiplier)-1]}=0'
else:
    result += '=0'
if multiplier [0] == 0:
    result = result.replace('+', '', 1)
equation = result.replace ('**1', '')
print (equation)
with open ('hwtask19.txt', 'w') as file:
    file.write (equation)
