# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]
N=int(input())
from random import randint
A=[0]*N
for i in range(N):
    A[i]=randint(-100,100)
print(A)
A=sorted(A)[::-1]
print(A)
