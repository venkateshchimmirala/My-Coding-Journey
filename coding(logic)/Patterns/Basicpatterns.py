'''If Input is 5 then Print 
1 0 0 0 0
0 2 0 0 0
0 0 3 0 0
0 0 0 4 0
0 0 0 0 5'''
n=int(input())
if n>0:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                print(i,end=' ')
            else:
                print("0",end=' ')
        print()
else:
    print('Invalid Input')

'''If Input is 5 then Print 
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5'''
n=int(input())
if n>0:
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,end=' ')
        print()
else:
    print('InValid InPut')

'''If Input is 5 and 5 then Print 
1*2*3*4*5
6*7*8*9*10
11*12*13*14*15
16*17*18*19*20
21*22*23*24*25'''
n=int(input())
n1=int(input())
if n<=0 and n1<=0:
    print("Invalid Row and Column Values")
elif n<=0:
    print("Invalid Row Value")
elif n1<=0:
    print("Invalid Column Value")
else:
    c=0
    for i in range(1,n+1):
        cc=0
        for j in range(1,n1+1):
            c+=1
            cc+=1
            if cc>1:
                print(end="*")
            print(c,end='')
        print()

'''If Input is 5 4 then Print 
* * * *
* * * *
* * * *
* * * *
* * * *'''
n=int(input())
n1=int(input())
if n>0 and n1>0:
    for i in range(1,n+1):
        for j in range(1,n1+1):
            print("*",end=' ')
        print()
else:
    print("Invalid Inputs")

'''If Input is 5 then Print 
55555
54444
54333
54322
54321'''
n=int(input())
if n==0:
    print("InvaliD Input")
else:
    n=abs(n)
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            if i==j:
                print(i,end='')
            elif i>j:
                print(i,end='')
            else:
                print(j,end='')
        print()

'''If Input is 5 then Print 
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1'''
n=int(input())
if n>0:
    c=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(c,end=' ')
            if c==1:
                c=0
            else:
                c=1
        print()
        if c==1:
            c=0
        else:
            c=1
else:
    print("Invalid Input")

'''If Input is 5 then Print 
1 2 3 * 5
6 7 * 9 10
11 * 13 14 15
* 17 18 19 *
21 22 23 * 25'''
n=int(input())
if n>0:
    c=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if c%4==0:
                print("*",end=' ')
            else:
                print(c,end=' ')
            c+=1
        print()
else:
    print('Given Value is Invalid')
