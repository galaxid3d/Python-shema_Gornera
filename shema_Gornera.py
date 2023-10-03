# 19.11.2015 by galaxid3d
# Проверяет, является ли число корнем многочлена по схеме Горнера

def show_polinom(n, k, number_pass): # делает правильное отображение x^n-степени*коэффициент,т.е. x^0 не пишет или 0*x^n
    res = ""
    if k != 0:
        if number_pass != 0:  # если сейчас максимальная степень,то знак не ставим
            if k > 0: res = " + "
            else: res = " - "; k = -k
        if k != 1:
            res += str(k)
            if n != 0: res += "*"
        if k == 1 and n == 0: res += str(k)
        if n == 1: res += 'x'
        elif n != 0: res += ('x^' + str(n))
    return res

n = int(input("Введите наибольшую степень многочлена: "))
a_G = [[], []]
tmp = str()
for i in range(n, -1, -1):  # "+1"-т.к. есть еще нулевая степень
    a_G[0].append(float(input("Введите коэффициент для x^" + str(i) + ": ")))
    tmp = tmp + show_polinom(i, a_G[0][n - i], (n - i))
print("Вы ввели многочлен: ", tmp)

while True:
    print("______________________")
    x = float(input("Введите корень: "))
    a_G[1] = []
    for i in range(n + 1): # Вычисляем числа во второй строке схемы Горнера
        if i == 0: a_G[1].append(a_G[0][i])
        else: a_G[1].append(a_G[1][i - 1] + x * a_G[0][i])

    print(' ' * len(str(x)), '|', end="")  # Делаем отступ слева такой же длины, как и x
    for i in range(n + 1):  # проходим строки таблицы: всего сделал 2 строки: 1-коэффициенты, а 2-меняется,в зависимости от x
        print(a_G[0][i], end=" ")
    print()
    print(x, "|", end="")

    for i in range(n + 1):
        print(a_G[1][i], end=" ")
    print()
    if a_G[1][-1] == 0: print('x =', x, 'является корнем многочлена')
