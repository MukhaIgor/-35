# Дано шість різних чисел. Визначити максимальне з них. (Визначити
# функцію, яка знаходить максимум з двох різних чисел.).

import numpy as np  # імпортируємо бібліотеку нампай
import random

b = np.zeros(6, dtype=int)
for i in range(6):  # проходимся по елементам масиву
    b[i] = random.randint(0, 20)
print(b)


def max():  # заводимо нашу функцію для пошуку максимального числа масиву
    count = 0
    for i in range(len(b)):
        if b[i] > count:
            count = b[i]
    print('максимальне число', count)


print(max())
