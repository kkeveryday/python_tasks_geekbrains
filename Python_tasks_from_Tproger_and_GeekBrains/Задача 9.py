# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

import datetime

seconds = 1339521878
result = datetime.datetime.fromtimestamp(seconds)  # UNIX
print(result)
