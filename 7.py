"""Визначити суму всіх парних елементів одновимірного масиву."""
import numpy as np
import random

b = np.array([random.randint(0, 10) for i in range(5)])  # заводимо масив
count = 0
print(b)
for i in range(len(b)):
    if b[i] % 2 == 0:
        count += b[i]  # додаємо всі парні елементи масиву
print(count)
