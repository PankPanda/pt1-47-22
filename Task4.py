"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных
 друг другу. Считается, что любые два элемента, равные друг другу
 образуют одну пару, которую необходимо посчитать.
 Входные данные - строка из чисел, разделенная пробелами.
 Выходные данные - количество пар.
 Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар"""

numbers = input("Введите массив чисел: ")
sort_list = numbers.split()
counter = 0
for i in range(len(sort_list)):
    for a in range(i + 1, len(sort_list)):
        if sort_list[i] == sort_list[a]:
            counter += 1
print("Колличество пар: ", counter)
