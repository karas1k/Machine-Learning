# # -*- coding: utf-8 -*-
# Задача 1. Минимизация гладкой функции
#
#     1.Рассмотрим все ту же функцию из задания по линейной алгебре:
#       f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2), но теперь уже на промежутке [1, 30]
#     2.В первом задании будем искать минимум этой функции на заданном промежутке с помощью scipy.optimize.
#       Разумеется, в дальнейшем вы будете использовать методы оптимизации для более сложных функций,
#       а f(x) мы рассмотрим как удобный учебный пример.
#     3.Напишите на Питоне функцию, вычисляющую значение f(x) по известному x.
#       Будьте внимательны: не забывайте про то, что по умолчанию в питоне целые числа делятся нацело, и о том,
#       что функции sin и exp нужно импортировать из модуля math.
#     4.Изучите примеры использования scipy.optimize.minimize в документации Scipy (см. "Материалы")
#     5.Попробуйте найти минимум, используя стандартные параметры в функции scipy.optimize.minimize
#       (т.е. задав только функцию и начальное приближение).
#       Попробуйте менять начальное приближение и изучить, меняется ли результат.
#     6.Укажите в scipy.optimize.minimize в качестве метода BFGS
#       (один из самых точных в большинстве случаев градиентных методов оптимизации),
#       запустите из начального приближения x=2. Градиент функции при этом указывать не нужно – он будет оценен численно.
#       Полученное значение функции в точке минимума - ваш первый ответ по заданию 1, его надо записать с точностью до 2 знака после запятой.
#     7.Теперь измените начальное приближение на x=30. Значение функции в точке минимума -
#       ваш второй ответ по заданию 1, его надо записать через пробел после первого, с точностью до 2 знака после запятой.
#     8.Стоит обдумать полученный результат. Почему ответ отличается в зависимости от начального приближения?
#       Если нарисовать график функции (например, как это делалось в видео, где мы знакомились с Numpy, Scipy и Matplotlib),
#       можно увидеть, в какие именно минимумы мы попали. В самом деле, градиентные методы обычно не решают
#       задачу глобальной оптимизации, поэтому результаты работы ожидаемые и вполне корректные.


import numpy as np
import math
import matplotlib.pylab as plt
from scipy.optimize import minimize

# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)
def functQuiz(x):
    f = np.sin(x / 5.) * np.exp(x /10.) + 5 * np.exp(-x /2.)
    return f

# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)
def functQuizMath(x):
    f = math.sin(x / 5.) * math.exp(x /10.) + 5 * math.exp(-x /2.)
    return f

xPoints = np.arange(1, 30, 0.1)

# 1
# yPoints = []
# for x in xPoints:
#     yPoints.append(functQuiz(x));
# 2
fx = functQuiz
yPoints = map(fx, xPoints)
plt.plot(xPoints, yPoints)


#     5.Попробуйте найти минимум, используя стандартные параметры в функции scipy.optimize.minimize
#       (т.е. задав только функцию и начальное приближение).

for x in range(30):
    k = minimize(fx, x)
    print 'iteration - ', x
    print k
    print '------------------'

# iteration -  5
#       fun: 1.745268290331984
#  hess_inv: array([[ 6.0552088]])
#       jac: array([ -4.47034836e-08])
#   message: 'Optimization terminated successfully.'
#      nfev: 21
#       nit: 6
#      njev: 7
#    status: 0
#   success: True
#         x: array([ 4.13628832])

 #    iteration -  27
 #      fun: -11.898894665974735
 # hess_inv: array([[ 1.67456939]])
 #      jac: array([  2.74181366e-06])
 #  message: 'Optimization terminated successfully.'
 #     nfev: 15
 #      nit: 4
 #     njev: 5
 #   status: 0
 #  success: True
 #        x: array([ 25.88019774])

#     6.Укажите в scipy.optimize.minimize в качестве метода BFGS
#       (один из самых точных в большинстве случаев градиентных методов оптимизации),
#       запустите из начального приближения x=2. Градиент функции при этом указывать не нужно – он будет оценен численно.
#       Полученное значение функции в точке минимума - ваш первый ответ по заданию 1, его надо записать с точностью до 2 знака после запятой.


x0 = 30
k = minimize(fx, x0, method='BFGS')
print 'BFGS - ', x0
print k
print '------------------'


# BFGS -  2
#       fun: 1.7452682903447336
#  hess_inv: array([[ 5.98752645]])
#       jac: array([ -2.04145908e-06])
#   message: 'Optimization terminated successfully.'
#      nfev: 21
#       nit: 6
#      njev: 7
#    status: 0
#   success: True
#         x: array([ 4.13627628])

# BFGS -  30
#       fun: -11.898894665981265
#  hess_inv: array([[ 1.67840334]])
#       jac: array([  1.19209290e-07])
#   message: 'Optimization terminated successfully.'
#      nfev: 18
#       nit: 5
#      njev: 6
#    status: 0
#   success: True
#         x: array([ 25.88019347])

plt.show()