# colors = ['red', 'blue', 'green']
# data = open ('file.txt', 'w')
# data.writelines(colors)
# data.write('kjeh f\n')
# data.close

# with open ('file1.txt', 'w') as data:
#     data.write ('line \n')
#     data.write ('line 2\n')


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print (line)
# data.close

# def concatenatio (*params):
#     res: str = '' #clear data type indiication
#     for item in params:
#         res += item
#     return res

# print (concatenatio ('a', 'b', 'c'))
# print (concatenatio('a', '1'))

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib (n-1) + fib (n-2)

# list = []
# for e in range (1, 10):
#     list.append (fib(e))
# print (list)

# a = (1, 2, 3)
# print (a)
# print (a[2])

# t = tuple(['red', 'blue', 'green'])  # преобразовываем список в кортеж
# red, green, blue = t # распаковка кортежа в отдельные элементы, порядок останется
# print ('r: {} g: {} b: {}'.format (red, green, blue))

# dictionary = {}
# dictionary = \
#     {
#         'up': 1,
#         'left': 2,
#         'down': 3
#     }
# print (dictionary)
# print (dictionary['up'])
# # for item in dictionary.keys():
# #     print (item)
# # for item in dictionary.values():
# #     print(item)
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

# colors = {'red', 'blue', 'green'}
# print(colors)
# colors.add ('red')
# print(colors)
# colors.add ('gray')
# print(colors)
# colors.remove ('red')
# print(colors)
# colors.discard ('red')
# print(colors)
# colors.clear()
# print(colors)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# print(c)
# u = a.union(b) # unite sets, only unique values are saved
# print (u)
# i = a.intersection(b) # shows same values that boths sets contain
# print (i)
# d1 = a.difference(b) # what set are contains and set b not
# d2 = b.difference(a)
# print (d1)
# print(d2)

# q = a \
#     .union (b) \
#     .difference(a.intersection(b))
# print (q)

list = [1, 2, 3, 4]
list.pop(1)
print (list)
list.insert(1, 11)
print (list)