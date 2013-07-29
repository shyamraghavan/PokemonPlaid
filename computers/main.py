__author__ = 'shyam'


def factorial(num):
    ret = 1
    while num > 1:
        ret = num * ret
        num -= 1
    return ret

big_num = factorial(15151)
total = 0
x = 2

while True:
    total = total + (big_num / (factorial(x) * factorial(15151-x)))
    x += 2
    if x == 15150:
        break

final = ''

str(total)
a = 0

while True:
    final = final + total[a]
    a += 500
    if a == len(str(total)) / 500 * 500:
        break

print final