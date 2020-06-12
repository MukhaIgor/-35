'''У одновимірному масиві зберігаються відомості про вартість 12-ти різних
предметів. Визначити загальну вартість всіх предметів.'''
import numpy as np
import random

b = np.array([random.randint(0, 1000) for i in range(12)])  # заводимо масив
count = 0
print(b)
for i in range(len(b)):
    count += b[i]  # додаємо всі елементи масиву
print(count)
