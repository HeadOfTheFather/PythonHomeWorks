#Требуется вывести все целые степени двойки (т.е. числа вида 2k), непревосходящие числа N.


n = int(input())
x = 0
while 2 ** x <= n:
    print(2 ** x)
    x += 1