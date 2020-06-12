# Знайти значення виразу:
# 2 ∗ 5! + 3 ∗ 8!/6! + 4!
# де n! означає факторіал числа n (n! = 1 * 2 * ... * n). (Визначити функцію для
# розрахунку факторіала натурального числа.).

def factorial(a):
    factor = 1
    while a > 1:
        factor *= a
        a -= 1
    return factor


b = (2 * factorial(5) + 3 * factorial(8)) / (factorial(6) + factorial(4))
print(b)
