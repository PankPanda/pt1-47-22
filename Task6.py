# Напишите программу, запрашивающую у пользователя целые числа,
# пока он не оставит строку ввода пустой. После окончания ввода на
# экран должны быть выведены сначала все отрицательные числа,
# которые были введены, затем нулевые и только после этого
# положительные. Внутри каждой группы числа должны отображаться
# в той последовательности, в которой были введены пользователем.
# Например, если он ввел следующие числа: 3, -4, 1, 0, -1, 0 и -2, вывод
# должен оказаться таким: -4, -1, -2, 0, 0, 3 и 1. Каждое значение должно
# отображаться на новой строке.
num_input = input("Введите число, или оставьте строку пустой: ")
num1, num2, num3 = [], [], []
while num_input != '':
    if int(num_input) < 0:
        num1.append(int(num_input))
        num_input = input("Следующее число: ")
    elif int(num_input) == 0:
        num2.append(int(num_input))
        num_input = input("Следующее число: ")
    elif int(num_input) > 0:
        num3.append(int(num_input))
        num_input = input("Следующее число: ")
result = num1 + num2 + num3
for i in result:
    print(i, end='\n')
