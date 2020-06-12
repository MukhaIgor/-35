"""Дан двовимірний масив розмірності n x n. Визначити:
a) суму всіх елементів третього рядка масиву;
b) суму всіх елементів s-го стовпця масиву."""
import numpy as np
import random as rnd

n = int(input('Введіть розмірність масиву n*n: '))

A = np.zeros((n, n), int)

for i in range(len(A)):
    for j in range(len(A)):
        A[i, j] = rnd.randint(0, 20)
print('Ваш масив згенеровано: ', A)
sum=0
for i in range(len(A)):
    for j in range(len(A)):
        if i == 3:
            sum+=A[i,j]
print(sum)
