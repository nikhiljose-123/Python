n=int(input('ente a number'))
bin=''
digit=0

while(n>0):
    digit=n%2
    n//=2
    bin=str(digit)+bin
print(bin)