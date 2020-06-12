"""З'ясувати, чи вірно, що сума елементів одновимірного масиву є невід'ємне
число."""
import numpy as np
import random

b = np.array([random.randint(-15, 15) for i in range(12)])  # заводимо масив
count = 0
print(b)
t = False
for i in range(len(b)):
    count += b[i]  # додаємо всі елементи масиву
    if count > 0:
        t = True
    else:
        t = False
print(count)
print(t)
