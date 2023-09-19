# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd
data = pd.read_csv('***.csv')
unique_values = {value: index for index, value in enumerate(data['whoAmI'].unique())}
one_hot_data = pd.DataFrame(columns=unique_values.keys())
for value in data['whoAmI']:
    one_hot_data.loc[len(one_hot_data)] = [1 if i == value else 0 for i in unique_values.keys()]
one_hot_data.head()