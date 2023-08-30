# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Решение 1

# n = "a a a b c a a d c d d".split()
# s = ''
# for i in range(len(n)):
#     s = n[:i]
#     if s.count(n[i]) == 0:
#         print(n[i], end=' ')
#     else:
#         print(f'{n[i]}_{s.count(n[i])}', end=' ')

# Решение 2

# all_letters = 'a b c a d b d d b c a a'.split()

# letters_count = {}

# result_str = ''

# for letter in all_letters:
#     if letter not in letters_count:
#         letters_count[letter] = 1
#         result_str += f'{letter} '
#     else:
#         result_str += f'{letter}_{letters_count[letter]} '
#         letters_count[letter] += 1
# print(result_str)

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# a = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".split()
# print(len(set(a)))

# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# # Решение 1

# list_1 = []
# s = 1
# while s > 0:
#     s = int(input('введите число: '))
#     list_1.append(s)
# print(max(list_1))

# # Решение 2

# m = 0
# while (n := int(input())) != 0:
#     if n > m:
#         m = n
# print(m)
