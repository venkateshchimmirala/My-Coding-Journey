'''If Input is 5 then Print
*
**
***
****
*****'''
n=int(input())
if n>0:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end='')
        print()
else:
    print("Invalid Input")

'''If Input is 5 then Print
*****
 ****
  ***
   **
    *'''
n=int(input())
if n>0:
    for i in range(n,0,-1):
        print(" "*(n-i),end='')
        for j in range(1,i+1):
            print("*",end='')
        print()
else:
    print("Invalid Input")

'''If Input is 5 then Print
    *
   **
  ***
 ****
*****'''
n=int(input())
if n>0:
    for i in range(1,n+1):
        print(' '*(n-i),end='')
        for j in range(1,i+1):
            print("*",end='')
        print()
else:
    print("Invalid Input")

'''If Input is 4 then Print
A
B C
D E F
G H I J'''
n=int(input())
n=abs(n)
if n==0:
    print('Invalid Input')
elif n<1 or n>6:
    print("Range Exceeded")
else:
    c=65
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(c),end=' ')
            c+=1
        print()

'''If Input is 5 then Print
10 10 10 10 10
8 8 8 8
6 6 6
4 4 
2'''
n=int(input())
if n>0:
    c=n*2
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(c,end=' ')
        print()
        c-=2
else:
    print("Invalid Input")

'''If Input is 5 then Print
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15'''
n=int(input())
if n>0:
    c=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(c,end=' ')
            c+=1
        print()
else:
    print("Invalid Input")

'''If Input is 6 then Print
1 2 3 4 5 6
5 4 3 2 1
1 2 3 4
3 2 1
1 2
1'''
n=int(input())
if n>0:
    for i in range(1,n+1):
        if i%2==0:
            d=c-1
        else:
            c=0
        for j in range(1,n-i+2):
            if i%2==1:
                c+=1
                print(c,end=' ')
            else:
                print(d,end=' ')
                d-=1
        print()
else:
    print("Invalid Input")

'''If Input is 5 then Print
2
3 5
6 8 10
11 13 15 17
18 20 22 24 26'''
n=int(input())
if n==0:
    print("Invalid Input")
else:
    n=abs(n)
    c=2
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(c,end=' ')
            c+=2
        c-=1
        print()

'''If Input is 4 and 1 then Print
1 – 1
2 3 – 5
4 5 6 – 15
7 8 9 10 – 34'''
n=int(input())
n1=int(input())
if n<=0 and n1<=0:
    print("Invalid Inputs")
elif n1<=0:
    print("Invalid Starting Value")
elif n<=0:
    print("Invalid Row Input")
else:
    c=n1
    for i in range(1,n+1):
        s=0
        for j in range(1,i+1):
            print(c,end=' ')
            s+=c
            c+=1
        print("-",end=' ')
        print(s,end='')
        print()

'''If Input is 5 then Print
5 4 3 2 1
4 3 2 1 
3 2 1
2 1
1'''
n=int(input())
if n>0:
    for i in range(n,0,-1):
        c=i
        for j in range(1,i+1):
            print(c,end=' ')
            c-=1
        print()
else:
    print("Invalid Input")

'''If Input is 4 and 5 then Print
5 @ 5 – odd
7 9 @ 16 – even
11 13 15 @ 39 – odd
17 19 21 23 @ 80 – even
'''
n=int(input())
n1=int(input())
if n<=0 and n1%2!=1:
    print("Invalid Inputs")
else:
    if n>0:
        if n1%2!=1:
            print("Invalid Starting Value")
        else:
            c=n1
            for i in range(1,n+1):
                s=0
                for j in range(1,i+1):
                    print(c,end=' ')
                    s+=c
                    c+=2
                print("@",end=' ')
                print(s,end=' - ')
                if s%2==0:
                    print("Even",end='')
                else:
                    print("Odd",end='')
                print()
    else:
        print("Invalid Row Value")