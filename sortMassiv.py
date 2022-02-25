def summ(m):
    s = 0
    while m > 0:
        s += m % 10
        m = m // 10
    return s


from random import random

N = 10
a = [0] * N
for i in range(N):
    a[i] = int(random() * 40) + 10
    print('%4d' % a[i], end='')
print()

for i in range(N - 1):  # количество переборов 9
    for j in range(N - i - 1):  # при первом переборе i=0
        if summ(a[j]) > summ(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]

for i in range(N):
    print('%4d' % a[i], end='')
print()

for i in range(N):
    print('%4d' % summ(a[i]), end='')

print()
