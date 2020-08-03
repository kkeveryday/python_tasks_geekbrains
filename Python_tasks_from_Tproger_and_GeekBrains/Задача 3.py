# Отсортируйте словарь по значению в порядке возрастания и убывания.

d = {0: '1',
     3: '4',
     85: '86',
     2: '3',
     55: '56'}
d_list = list(d.items())
d_list.sort(key=lambda i: i[1])
print(d_list)
d_list.sort(key=lambda i: i[1], reverse=True)
print(d_list)
