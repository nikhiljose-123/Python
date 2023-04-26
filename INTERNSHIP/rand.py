import random
r=random.randint(10,50)
n=int(input('enter:'))
while n!=r:
    if n<r:
        print('hi')
        n=int(input('enter again'))
    elif n>r:
        print('hi')
        n = int(input('enter again'))
    else:
        break
print('you guessed crct')