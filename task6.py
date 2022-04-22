"""Во входной строке записан текст. Словом считается
последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или
символами конца строки. Определите, сколько различных слов
содержится в этом тексте."""

import string

sentence = input("Введите предложение: ")
for i in string.punctuation:
    sentence = sentence.replace(i, " ")
sentence = set(sentence.split())
print(f"Число слов: {len(sentence)}")
