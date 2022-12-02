# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

import math
d = input('enter precision as float, e.g. 0.01, 0.0001, etc: ' )
print (round(math.pi, len(d)-2))
