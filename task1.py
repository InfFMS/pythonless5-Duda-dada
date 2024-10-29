# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.


from random import randint
N=int(input())
A=[0]*N
for i in range(N):
    A[i]=randint(0, 1000)
print (A)
l=len(A)
print (l, 'длина')
g=A[-1]
print (g, 'последний элемент списка')
o=A[::-1]
print (o, 'список в обратном порядке')
for it in [111, 222, 333, 444, 555, 666, 777, 888, 999]:
    if it in A:
        print ('YES')
else:
    print ('NO')
m=(A[1:-1])
print (m, 'без первого и последнего элемента')

