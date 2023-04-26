import math

a = int(input('enter the value  for a:'))

b = int(input('enter the value  for b:'))
c = int(input('enter the value  for c:'))

d = ((b * b)-(4 * a * c))
if (d==0):
    print('roots are real and equal')
    r = (-b)/(2 * a)
    print(r)
elif (d>0):
    print('roots are real and distinct')
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print(r1)
    print(r2)

else:
    print('roots are imaginary')

print(d)

