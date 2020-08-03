# Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874,
# 'f': 20}.

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
list_d = list(my_dict.items())
list_d.sort(key=lambda i: i[1], reverse=True)
keys, _ = zip(*list_d)
print(list(keys)[:3])
