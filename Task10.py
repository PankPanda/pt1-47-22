"""Дан список целых чисел. Требуется переместить все ненулевые
 элементы в левую часть списка, не меняя их порядок, а все нули - в
 правую часть. Порядок ненулевых элементов изменять нельзя,
 дополнительный список использовать нельзя, задачу нужно
 выполнить за один проход по списку. Распечатайте полученный
 список."""

number_list = list(map(int, input('Введите числа через пробел: ').split()))
number_list.sort(key=lambda x: not x)
print(number_list)
