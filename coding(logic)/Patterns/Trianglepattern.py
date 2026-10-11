'''If Input is 5 then Print
2
2 3
2 3 5
2 3 5 7
2 3 5 7 11'''
n=int(input())
n=abs(n)
if n>0:
    l=[]
    for i in range(1,60):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            l.append(i)
    for i in range(1,n+1):
        for j in range(0,i):
            print(l[j],end=' ')
        print()
else:
    print("Invalid Input")

'''1
3*2
4*5*6
10*9*8*7
11*12*13*14*15'''
n=int(input())
if n==0:
    print("Invalid Input")
else:
    n=abs(n)
    c=0
    for i in range(1,n+1):
        cc=0
        if i%2==0:
            d=c+i
        for j in range(1,i+1):
            c+=1
            if i%2==1:
                cc+=1
                if cc>1:
                    print(end='*')
                print(c,end='')
            else:
                cc+=1
                if cc>1:
                    print(end='*')
                print(d,end='')
                d-=1
        print()

'''         01
         02 03
      04 05 06
   07 08 09 10
11 12 13 14 15'''
n=int(input())
if n>0:
    c=1
    for i in range(1,n+1):
        print("   "*(n-i),end='')
        for j in range(1,i+1):
            print(f'{c:02}',end=' ')
            c+=1
        print()
else:
    print('Invalid Input')

'''         G
          G F
        G F E
      G F E D
    G F E D C
  G F E D C B
G F E D C B A'''
n=int(input())
if n<=0:
    print("Invalid Input")
elif n<1 or n>26:
    print("Invalid Row Value")
else:
    for i in range(1,n+1):
        c=64+n
        print("  "*(n-i),end='')
        for j in range(1,i+1):
            print(chr(c),end=' ')
            c-=1
        print()

'''1
1 2
1 2 3
1 2 3 5
1 2 3 5 8
1 2 3 5 8 13'''
n=int(input())
n=abs(n)
l=[]
cc=0
a,b=1,2
while cc<20:
    l.append(a)
    cc+=1
    c=a+b
    a=b
    b=c
if n>0:
    for i in range(1,n+1):
        for j in range(0,i):
            print(l[j],end=' ')
        print()
else:
    print("Invalid Input")

'''1
2 6
3 7 10
4 8 11 13
5 9 12 14 15'''
n=int(input())
if n>0:
    c=1
    for i in range(1,n+1):
        k=i
        d=n-1
        for j in range(1,i+1):
            print(k,end=' ')
            k+=d
            d-=1
        print()
else:
    print("Invalid Input")

'''
* * * * *
 * * * *
  * * *
   * *
    *
    '''
n=int(input())
if n==0:
    print("Invalid Input")
else:
    n=abs(n)
    for i in range(n,0,-1):
        print(" "*(n-i),end='')
        for j in range(1,i+1):
            print("*",end=' ')
        print()

''' 1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1'''
n=int(input())
if n==0:
    print("Invalid Input")
elif n<0:
    print("Given Input is Negative")
else:
    for i in range(1,n+1):
        k=1
        print(' '*(n-i),end='')
        for j in range(1,i+1):
            print(k,end=' ')
            k=(k*(i-j))//j
        print()

'''1
  212
 32123
4321234'''
n=int(input())
if n==0:
    print("Oh! I got Zero(0)")
else:
    n=abs(n)
    for i in range(1,n+1):
        print(" "*(n-i),end='')
        for j in range(i,0,-1):
            print(j,end='')
        for j in range(2,i+1):
            print(j,end='')
        print()

'''     01
      02  03
    04  05  06
  07  08  09  10
11  12  13  14  15'''
n=int(input())
if n==0:
    print("Invalid Input")
else:
    n=abs(n)
    c=1
    for i in range(1,n+1):
        print("  "*(n-i),end='')
        for j in range(1,i+1):
            print(f'{c:02}',end='  ')
            c+=1
        print()