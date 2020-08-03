# Напишите программу для слияния нескольких словарей в один.


def merge(*kwargs):
    result = {}
    for d in kwargs:
        result.update(d)
    return result


dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}
print(merge(dict_a, dict_b, dict_c))
