# def calc1 (x):
#     return x+10
# def calc2 (x):
#     return x*10
# def math (op, x):
#     print (op(x))
# math (calc2, 10)

# f = lambda x: x +10
# math (f, 10)
# math (lambda x: x +10, 20)

# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# x = (lambda i: i**2)
# list2 = [(i, x(i)) for i in list1 if i%2==0]
# print (list2)

# li = [x for x in range (1,20)]
# li = list (map(lambda x: x+10, li))
# print (li)

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x%2, data))
# print (res)

# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# l3 = ['!', ',', '.']
# m = list(zip (l1, l2, l3))
# print(m)

ll1 = ['abc', 'def', 'ghi']
result = list(enumerate(ll1))
print(result)