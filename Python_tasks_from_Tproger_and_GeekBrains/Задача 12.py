# Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить
# невозможно, выбросите исключение.

import os


def get_extension(file):
    try:
        filename, file_extension = os.path.splitext(file)
        if file_extension == '':
            raise ValueError
    except ValueError:
        return 'У файла нет расширения'
    return file_extension


print(get_extension('test.exe'))
