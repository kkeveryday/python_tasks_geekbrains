# При заданном целом числе n посчитайте n + nn + nnn + ...

n = int(input())
s = 0
for i in range(1, n + 1):
    s += int(str(n) * i)
print(s)

