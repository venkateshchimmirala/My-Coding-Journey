'''Harmonic Progression Series Nth Term'''
s=int(input())
d=int(input())
n=int(input())
if n>0:
    p=1/(s+(n-1)*d)
    print(f'{p:.2f}')
else:
    print('InvaliD InPut')

'''Sum of Arithmetic Progression Series'''
s=int(input())
d=int(input())
n=int(input())
ss=0
c=0
if n>0:
    for i in range(n):
        c+=1
        if c>1:
            print(end=' + ')
        print(s+(i*d),end='')
        ss=ss+(s+(i*d))
    print(f' = {ss}.')
else:
    print('Invalid input.')

'''LCM of a given two numbers'''
a=int(input())
b=int(input())
if a>0 and b>0:
    k=max(a,b)
    # print(k)
    h=k
    while True:
        if k%a==0 and k%b==0:
            print(k)
            break
        k+=h
else:
    if a<=0 and b>0:
        print("Invalid First Input")
    elif b<=0 and a>0:
        print("InValid Second Input")
    else:
        print("Invalid Inputs.")

'''Sum of Geometric Progression Series'''
a=int(input())
r=int(input())
n=int(input())
s=0
if n>0:
    for i in range(n):
        s=s+a*(r**i)
    print(s)
else:
    print("Invalid Input")

'''Harmonic Progression Series'''
a=int(input())
b=int(input())
n=int(input())
c=0
if n>0:
    for i in range(n):
        c+=1
        if c>1:
            print(end=', ')
        p=1/(a+(i*b))
        print(f'{p:.2f}',end='')
else:
    print("Invalid Input")

'''Geometric Progression Series'''
a=int(input())
b=int(input())
n=int(input())
c=0
if n>0:
    for i in range(n):
        c+=1
        if c>1:
            print(end=', ')
        print(a*(b**i),end='')
    print('.')
else:
    print('Invalid Input.')

'''GCD of a given three numbers'''
a=int(input())
b=int(input())
c=int(input())
if a<=0 and b<=0 or c<=0:
    print("Invalid Inputs")
elif a>0 and b>0 and c>0:
    l=min(a,b,c)
    for i in range(l,0,-1):
        if a%i==0 and b%i==0 and c%i==0:
            print(i)
            break
elif a<=0:
    print("Invalid First Input")
elif b<=0:
    print("Invalid Second Input")
elif c<=0:
    print("Invalid Third Input")

'''LCM of a given three numbers'''
n1=int(input())
n2=int(input())
n3=int(input())
k=max(n1,n2,n3)
h=k
if n1>0 and n2>0 and n3>0:
    while True:
        if k%n1==0 and k%n2==0 and k%n3==0:
            print(k)
            break
        k+=h
else:
    if n1<=0 and n2>0 and n3>0:
        print("InvalId First Input")
    elif n2<=0 and n1>0 and n3>0:
        print("Invalid Second Input")
    elif n3<=0 and n1>0 and n2>0: 
        print("InvaliD ThirD Input")
    elif n1<=0 and n2<=0 or n3<=0:
        print('Sorry Invalid Inputs!')
