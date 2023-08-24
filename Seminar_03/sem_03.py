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
