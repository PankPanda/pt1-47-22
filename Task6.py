# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково). Число положительное
# целое, произвольной длины. Задача требует работать только с числами (без конвертации числа в строку или что-нибудь
# еще)

word = input("Введите слово: ")
if word == word[::-1]:
    print("Слово - полиндром.")
