# Домашнее задание к лекции «Открытие и чтение файла, запись в файл»
# Задание 1.

with open('file_hw/recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        number_of_products = int(file.readline())
        products = []
        for ingredient in range(number_of_products):
            rcp = file.readline().strip()
            ingredient_name, quantity, measure = rcp.split(' | ')
            products.append(
                    {'ingredient_name': ingredient_name,
                     'quantity': int(quantity),
                     'measure': measure}
                )
        cook_book[dish_name] = products
        file.readline()


# Задание 2.
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}
    print(shop_list)





# Задание 3

import os
# current = os.getcwd()
# folder = r'C:\Users\admin\Downloads\landing'
# file1 = r'C:\Users\admin\Downloads\landing\1.txt'
# file2 = r'C:\Users\admin\Downloads\landing\2.txt'
# file3 = r'C:\Users\admin\Downloads\landing\3.txt'
# full_path1 = os.path.join(current, folder, file1)
# full_path2 = os.path.join(current, folder, file2)
# full_path3 =os.path.join(current, folder, file3)
# all_files = [full_path1,full_path2, full_path3 ]
import os
folder = r'C:\Users\admin\Downloads\landing'
files = ['1.txt', '2.txt', '3.txt']
all_files = [os.path.join(folder,file) for file in files]

file_names_len = {}
for fi_le in all_files:
    with open(fi_le, encoding='utf-8') as f:
        file_names_len[fi_le] = len(f.readlines())
sorted_files = sorted(file_names_len.items(), key=lambda x: x[1])

with open('BigBosFile.txt', 'w', encoding='utf-8') as f:
    for file_data in sorted_files:
       fi_le = file_data[0]
       file_lines_count = file_data[1]
       f.write('{}\n{}\n'.format(fi_le, file_lines_count))
       with open(fi_le, encoding='utf-8') as source_file:
           f.write(source_file.read())
       f.write('\n')




