""" Замінити значення всіх елементів головної діагоналі квадратного
масиву нульовими значеннями."""

import numpy as np
import random as rnd

n = int(input('Введіть розмірність масиву n*n: '))

A = np.zeros((n, n), int)

for i in range(len(A)):
    for j in range(len(A)):
        A[i, j] = rnd.randint(0, 20)
print('Ваш масив згенеровано: ', A)
for i in range(len(A)):
    for j in range(len(A)):
        if i == j:
            A[i, j] = 0
print('Нова матриця: ', A)
