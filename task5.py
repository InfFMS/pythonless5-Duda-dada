# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
N=int(input())
A=[]
for i in range(N):
    b=int(input())
    A.append(b)
count=0
max=0
for it in A:
    if it>max:
        it=max
        count=1
    elif it==max:
        count+=1
print(count)