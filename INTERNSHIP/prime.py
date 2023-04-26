n=int(input('enter how many numbers:'))
count=0
flag=0
for i in range(n):
    number=int(input('enter the number:'))
    if(number%2==0):
        count+=1
    else:
        flag+=1
print('even numbers:',count)
print('odd numbers:',flag)