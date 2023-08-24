# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# Решение 1

# a = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(a)))

# Решение 2

# str1 = [1, 1, 2, 0, -1, 3, 4, 4]
# counter = 0
# for i in range(len(str1)):
#     if str1[i] not in str1[:i]:
#         counter += 1
# print(counter)



# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]

# Решение 1

# def shift_sequence(arr, k):
#     k = k % len(arr)
#     result = arr[len(arr)-k:] + arr[:len(arr)-k]
#     return result

# arr = [1, 2, 3, 4, 5]
# k = int(input("Введите шаг: "))
# print(shift_sequence(arr, k))

# Решение 2

# lst = [1, 2, 3, 4, 5]
# k = 6
# for i in range(k):
#     el = lst.pop()
#     lst.insert(0, el)
# print(lst)



# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Решение 1

# def print_unique_values(dictionary_list):
#     unique_values = set()
#     for dictionary in dictionary_list:
#         for value in dictionary.values():
#             unique_values.add(value)
#     print(unique_values)

# dictionary_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# print_unique_values(dictionary_list)

# Решение 2

# my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, \
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 

# all_val = []
# for now_dict in my_list:
#     for val in now_dict.values():
#         all_val.append(val)


# print(set(all_val))