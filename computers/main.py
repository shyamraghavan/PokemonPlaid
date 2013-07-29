__author__ = 'shyam'


def factorial(num):
    ret = 1
    while num > 1:
        ret = num * ret
        num -= 1
    return ret

big_num = factorial(15151)
sum = 0
x = 2

while True:
    sum = sum + (big_num / (factorial(x) * factorial(15151-x)))
    x += 2
    print sum
    print x
    if x == 15150:
        break

final = ''

print len(str(sum))

for a in xrange(0,len(str(sum))/500):
    final += str(sum)(a*500)

print final