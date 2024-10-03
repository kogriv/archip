
# my_list = [1, 2, 3, 4, 5]
# my_array = np.array(my_list)
# print(my_array)
# ar = np.arange(1,20,2)
# ar = np.linspace(1,10,19)
# ar = np.linspace(-5,5,10)
# ar = np.arange(10,0,-1)


# # На вход подаются 2 числа a и b в виде строки
# # чисел через пробел. Создайте массив NumPy,
# # содержащий числа от a до b включительно, кратные 3,
# # выведите его на экран.
# a, b = tuple(map(int,input("введите 2 числа: ").split()))
# # resa = a%3
# # resb = b%3
# # if a-resa+3>=b:
# #     ar = np.empty(0)
# # else:
# #     ar = np.arange(a-resa+3,b-resb+3,3)
# # Определяем первое число, кратное 3, начиная от a
# start = a if a % 3 == 0 else a + (3 - a % 3)
# # Создаем массив с шагом 3 от start до b включительно
# ar = np.arange(start, b + 1, 3)
# print(ar)

# # На вход подается целое число n.
# # Cоздайте массив из n случайных действительных
# # чисел в интервале от 0 до 1 не включительно.
# # Выведите массив на экран.
# np.random.seed(32)
# n = int(input())
# ar = np.random.rand(n)
# print(ar)


import numpy as np
# На вход подается целое число n>=1.
# Создайте массив, содержащий n первых
# простых чисел. Выведите его на экран.

def is_prime(num,primes):
    ...

# n = int(input())
# i = 1 # инкремент количества итераций
# primes = [2] # список простых чисел
# next_number = 2
# print('ищем количество:',n)
# while i<n:
#     print('-- итерация:',i)
#     if n==1:
#         i +=1
#     next_number += 1
#     next_number_divides_by = 1
#     divider_search = True
#     while divider_search:
#         print('ищем делители для ', next_number)
#         for pr in primes:
#             print('---- делитель:',pr)
#             if next_number%pr == 0:
#                 next_number_divides_by = pr
#                 print('----- делитель найден - число составное')
#                 divider_search = False
#                 break
#         # print('----- число делится на',next_number_divides_by)
        
#         if next_number_divides_by == 1:
#             print('----- делитель НЕ найден - число простое')
#             maxprime = next_number
#             primes.append(maxprime)
#             i +=1
            
#         divider_search = False
        

print(primes)