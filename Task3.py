# Вводится строка.
# Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde
# def", то должно быть выведено "abcdef".

sentence = input("Введите предложение:")
result = "".join(set(sentence))
result.split()
print(result)
