# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0,
# a1 = 1,
# ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fibonacci(a):
#     if a in (0, 1):
#         return 1
#     return fibonacci(a - 1) + fibonacci(a - 2)
# print(fibonacci(int(input("Введите число: "))))

# Задача 2 Меняем максимальные числа на минимальное

# Наше решение

# def izm(a):
#     maxx=max(a)
#     minn=min(a)
#     for i in range(len(a)):
#         if a[i] == maxx:
#             a[i] = minn
#     return a
# a = list(map(int, input().split()))
# print(*izm(a))

# Второе решение

# def rec(lst):
#     return [el if el != max(lst) else min(lst) for el in lst]

# Задача 3. Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def check_div(n):
#     if n < 4:
#         return "Yes"
#     for i in range(2, n//2 + 1):
#         if n % i == 0:
#             return "No"
#     return "Yes"
# n = int(input())
# print(check_div(n))

# Задача 4.Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def sort_f(n):
#     s = input()
#     if n != 1:
#         sort_f(n-1)
#     print(s, end=" ")

# n = int(input())
# sort_f(n)
