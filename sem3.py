# number = input()
# sum = 0
# for i in number:
#     if i != '.':
#         sum += int(i)
# print (sum)

with open('positions.txt', 'r') as f:
    positions = f.read().split('\n')
positions = list (map(int, positions))
print (positions)

# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['ssss', 'sngujn556', 56] -> Yes
# ['56', 'sgnbsb'] -> No

l = ['ssss', 'sngujn556', 56]
l1 = ['56', 'sgnbsb']

def get_digit(l):
    for el in l:
        if type(el) in (int, float):
            return 'yes'
    return 'no'
print(get_digit(l))
print(get_digit(l1))


# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

l2 = ["io", "h", "qwe", "asd", "zxc", "qwe", "ertqwe"]
l3 = ["йцу","йцу", "фыв", "йцу", "ячс", "цук", "йцукен", "йцу"]
l4 = ['123']
def get_2nd_str(l, string):
    if l.count(string) <= 1:
        print('-1')
    elif l.count(string) >= 2:
        first_ind = l.index(string)
        for i in range(first_ind + 1, len(l)):
            if l[i] == string:
                print(i, 'second_ind')
                return

get_2nd_str(l2, 'qwe')
get_2nd_str(l3, "йцу")
get_2nd_str(l4, '123')
