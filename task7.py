"""Анаграммами называются слова, образованные путем взаимной
перестановки букв. В английском языке, например,
анаграммами являются слова «live» и «evil», а в русском –
«выбор» и «обрыв». Напишите программу, которая будет
запрашивать у пользователя два слова, определять, являются ли
они анаграммами, и выводить на экран ответ."""


def anagramm_check(x: set, y: set):
    if x & y == x and y:
        print("Эти слова - анаграммы.")


word1 = set(input("Первое слово: ").lower())
word2 = set(input("Второе слово: ").lower())

anagramm_check(word1, word2)
