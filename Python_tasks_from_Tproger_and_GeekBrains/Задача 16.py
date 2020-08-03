# Выведите список файлов в указанной директории.

import os

lst = []
directory = "D:\PythonProjects"
for file_name in os.listdir(directory):
    lst.append(file_name)
print(lst)


