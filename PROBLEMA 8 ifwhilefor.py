a=eval(input('a='))
b=eval(input('b='))
c=eval(input('c='))
if(a+b>c and a+c>b and b+c>a):
    if(a==b and a==c):
        print("Triunghi echilateral")
    elif(a==b and a!=c):
        print("Triunghi isoscel")
    elif(a!=b and a==c):
        print("Triunghi isoscel")
    elif(b==c and b!=a):
        print("Triunghi isoscel")
    else:
        print("Triunghi scalen")
else:
    print("Nu se poate creea un triunghi")