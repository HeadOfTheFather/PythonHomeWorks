#Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*
#6 -> 1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

import math
print("Сколько всего журавликов сделали дети?: ")
S = int(input())
a = math.ceil(S / 100 * 16.6)
b = math.ceil(S / 100 * 66.6)
c = a
print(a, b, c)