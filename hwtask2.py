# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

x = bool(input('x = ' ))
y = bool(input('y = ' ))
z = bool(input('z = ' ))
if -(x or y or z) == -x and -y and -z:
    print ('True')
else:
    print ('False')