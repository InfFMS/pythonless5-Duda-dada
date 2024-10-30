# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
from random import randint

N = int(input())
A = [0] * N
for i in range(N):
    A[i] = str(randint(10, 100000))
print(A)


def res(a):
    for i in range(len(a) - 1):
        if a[i] != a[i + 1]:
            return None
    return int(a)


lst = list(map(res, A))
while True:
    if None in lst:
        lst.remove(None)
    else:
        break
print(lst)
