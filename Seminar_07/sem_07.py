# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Пример ввода и вывода данных представлены на следующем
# слайде

# transformation = lambda x:x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# print(transormed_values)



# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# orbis = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# def find_farthest_orbit (orb):
#     if orb[0]==orb[1]:
#         return 0
#     return orb[0]*orb[1]
# res = find_farthest_orbit(orbis[0])
# t = 0
# for i in range(1, len(orbis)):
#     if find_farthest_orbit(orbis[i])>res:
#         res =find_farthest_orbit(orbis[i])
#         t = i
# print(*orbis[t])

# Решение 2

# def max_orb(list1):
#     maxx=[(i[0]*i[1] if i[0]!=i[1] else 0) for i in list1 ]
#     return list1[maxx.index(max(maxx))]
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*max_orb(orbits))
# print(*max([(a,b) for a,b in orbits if a!=b], key=lambda x:x[0]*x[1]))

# Решение 3

# def max_orb(list_of_orbits):
#     s_orbits = [(x_1*x_2 if x_1 != x_2 else 0) for x_1, x_2 in list_of_orbits]
#     print(s_orbits)
#     print(max(s_orbits))
#     print(s_orbits.index(max(s_orbits)))
#     print(list_of_orbits[s_orbits.index(max(s_orbits))])
#     return list_of_orbits[s_orbits.index(max(s_orbits))]
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*max_orb(orbits))

# Решение 4

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(max([(a,b) for a,b in orbits if a!=b], key=lambda x: x[0]*x[1]))


# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristic, objects):
#     return(len(set(map(characteristic, objects)))) < 2

# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")