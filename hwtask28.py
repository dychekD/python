# f(x) = sin(x)^2 - cos(x)^2

from sympy.plotting import plot as plt
from sympy import *
x = Symbol('x')
fx = sin(x)**2 - cos(x)**2
# Определить корни
x1 = solveset(fx, x)
pprint (x1)
# Найти интервалы, на которых функция возрастает
pprint (solveset(diff(fx)>0, x))
# Найти интервалы, на которых функция убывает
pprint (solveset(diff(fx)<0, x))
# Построить график
p = plt(fx)
# Вычислить вершину
pprint (solveset(diff(fx), x))
# Определить промежутки, на котором f > 0
pprint(solveset(fx>0, x))
# Определить промежутки, на котором f < 0
pprint(solveset(fx<0, x))
