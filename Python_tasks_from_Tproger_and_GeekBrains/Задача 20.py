# С помощью анонимной функции извлеките из списка числа, делимые на 15.

lst = [15, 150, 1, 20, 300, 21, 3]
result = list(filter(lambda x: not x % 15, lst))
print(result)

