# Факториал

# a = int(input("Введите число: "))
# i = 2
# res = 1
# while i <= a:
#     res = res*i
#     i +=1
# print(res)

a = int(input("Введите число: "))
fib2 = 1
fib1 = 0
fib = 0
count = 1
while fib <= a:
    fib = fib1+fib2
    fib1, fib2 = fib2, fib
    count +=1
print(count if fib == a else -1)