# Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково
# читаются слева направо и справа налево.


def palindrome_1(value):
    value = str(value)
    l = len(value)
    count = 0
    if l % 2 == 0:
        for i in range(l):
            if count == l / 2:
                return 'Является палиндромом'
            if value[i] == value[0 - i]:
                count += 1
    else:
        for i in range(l // 2):
            if value[i] == value[0 - i]:
                count += 1
        if count == l // 2:
            return 'Является палиндромом'
    return 'Не является палиндромом'


def palindrome_2(value):
    if value == value[::-1]:
        return 'Является палиндромом'
    else:
        return 'Не является палиндромом'
    

print(palindrome_1('asdasd'))
print(palindrome_2('adddda'))

