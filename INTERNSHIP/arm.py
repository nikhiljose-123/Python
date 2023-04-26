num =int(input('enter a number:'))
order = len(str(num))
print(order)
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp=temp//10

if num==sum:
    print('The given num',num,'is armstrong')
else:
    print('The given num',num,'is not  armstrong')