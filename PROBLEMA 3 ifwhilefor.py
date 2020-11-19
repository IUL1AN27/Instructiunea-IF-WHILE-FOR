m=int(input('Introduceti numarul m '))
n=int(input('Introduceti numarul n '))
while n%m==0:
    n=n//m
if n==1:
    print('n este puterea lui m')
else:
    print('n nu este puterea lui m')