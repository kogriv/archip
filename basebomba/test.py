# b = [45, 37, 100]
# b.sort(reverse=True)
# print(b)
# c = input().split()
# print(c)
# c = map(int,c)
# print(c)
# c = list(c).sort()
# print(c)
# print(' '.join(map(str,sorted(list(map(int,input().split()))))))

# l = [3,4,5,6]
# # l.reverse()
# print(l.reverse())

# marks = [2, 3, 4, 3, 5, 2]
# marks[2:4] = 10, 20
# print(marks)

# v = [1205, 1101, 1434, 1320, 923, 874]
# vv = v[:3]
# print(vv)

# m = [0, 1, 2, 3, 4, 5, 6, 7]
# m.insert(1,'b')
# print(m)

# d = input()
# if d.endswith('7'): print('Y')
# else: print('N')

# s = input()
# l = ['t','h','o']
# if set(l).issubset(s):
#     print('ДА') 
# else: print('НЕТ')

# cities = input().split()
# if 'Москва' in cities:
#     cities.remove('Москва')

# a, b, c, d = (map(int,input().split()))
# if (c < a and d < b) or (c < b and d < a):
#     print('ДА')
# else: print('НЕТ')

# n = input()
# n1, n2 = sum(map(int,list(n[:3]))), sum(map(int,list(n[3:])))
# print(n1,n2)
# if n1 == n2:
#     print('ДА')
# else: print('НЕТ')

# """
# Работа светофора для пешеходов запрограммирована
# следующим образом: в начале каждого часа в течение
# трех минут горит зеленый сигнал, затем в течение
# двух минут – красный, в течение трех минут –
# опять зеленый и т. д., процесс повторяется.

# На вход программе подается вещественное число t,
# означающее время в минутах, прошедшее с начала
# очередного часа. Необходимо прочитать это число
# и определить, сигнал какого цвета горит для
# пешеходов в момент времени t (прочитанного из
# входного потока). На экран вывести сообщение (без кавычек):

#     "green" - для зеленого;
#     "red" - для красного.

# Sample Input:
# 12.5

# Sample Output:
# green
# """

# t = float(input())
# d = int(t)%5
# if d<=3:
#     print('green')
# else:
#     print('red')
