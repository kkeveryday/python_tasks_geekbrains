# Нужно проверить, все ли числа в последовательности уникальны.

lst = [int(i) for i in input().split(',')]
if len(lst) == len(set(lst)):
    print('Все числа уникальны')
else:
    print('Не все числа уникальны')


