'''Palindrome & Reverse'''
a=int(input())
t=a
if a==0:
    print("Zero")
elif a>=0:
    rev=0
    while a!=0:
        r=a%10
        rev=rev*10+r
        a//=10
    if rev==t:
        print("Given Number is Palindrome")
    else:
        print(f"Reverse of a Given Number is {rev}")
else:
    print("Invalid Input")


'''Sum of All Palindromes Between the Given Numbers'''
a=abs(int(input()))
b=abs(int(input()))
if a>b:
    a,b=b,a
if a==0 or b==0:
    print("INVALID Inputs")
else:
    s=c=0
    for i in range(a+1,b):
        t=i
        rev=0
        while t!=0:
            r=t%10
            rev=rev*10+r
            t=t//10
        if rev==i:
            s+=rev
            c+=1
    if c==0:
        print("No Palindrome Values")
    else:
        print(s)

'''Palindromes Between Numbers'''
a=int(input())
b=int(input())
if a>b:
    a,b=b,a
if a>=0 and b>=0:
    c=0
    for i in range(a+1,b):
        t=i
        rev=0
        while t!=0:
            r=t%10
            rev=rev*10+r
            t//=10
        if rev==i:
            c+=1
            print(i)
    if c==0:
        print("No Palindrome Values")
else:
    print("InvaliD InputS")

'''Palindrome or Not'''
a=int(input())
if a>0:
    t=a
    rev=0
    while t!=0:
        r=t%10
        rev=rev*10+r
        t//=10
    if rev==a:
        print("Palindrome")
    else:
        print("Not a Palindrome")
else:
    print("InvAlid Input")

'''Perfect Squares'''
a=abs(int(input()))
if a==0:
    print("Invalid Input")
else:
    b=False
    for i in range(1,a+1):
        if i*i==a:
            b=True
            break
        if i*i>a:
            break
    if b==True:
        print("Given Number is Perfect Square.")
    else:
        print("Given Number is Not a Perfect Square.")

'''Swapping of 2 Numbers'''
a=int(input())
b=int(input())
a,b=b,a
print(a)
print(b)

'''Reverse of A Given Number'''
a=int(input())
if a>0:
    rev=0
    while a!=0:
        r=a%10
        rev=rev*10+r
        a//=10
    print(rev)
else:
    print("InValid Input")

'''Alternative Palindrome Numbers In The Given Range'''
a=int(input())
b=int(input())
ac=c=0
if a>=0 and b>=0:
    for i in range(a,b+1):
        t=i
        rev=0
        while t!=0:
            r=t%10
            rev=rev*10+r
            t//=10
        if rev==i:
            ac+=1
            if ac%2==1:
                c+=1
                if c>1:
                    print(end=', ')
                print(i,end='')
    if ac==0:
        print("No Palindrome Values")
    else:
        print(".")
else:
    print("InvAlid InPUts")

'''Average of all Palindrome Numbers in the Given Range'''
a=abs(int(input()))
b=abs(int(input()))
if a==0 or b==0:
    print("INVALID Inputs")
elif a>b:
    print("Given Inputs are Swapped")
else:
    s=c=0
    for i in range(a,b+1):
        t=i
        rev=0
        while t!=0:
            r=t%10
            rev=rev*10+r
            t//=10
        if rev==i:
            c+=1
            s+=i
    if c==0:
        print("No Palindrome Values")
    else:
        print(f"{s/c:.2f}")

''' Sum of all Alternative Palindrome Numbers Between Given Numbers'''
a=abs(int(input()))
b=abs(int(input()))
if a>b:
    a,b=b,a
if a==0 or b==0:
    print("Invalid Inputs")
else:
    ac=s=c=0
    for i in range(a+1,b):
        t=i
        rev=0
        while t!=0:
            r=t%10
            rev=rev*10+r
            t//=10
        if rev==i:
            ac+=1
            if ac%2==1:
                s+=i
                c+=1
                if c>1:
                    print(end=' + ')
                if c==1:
                    print(f"Sum of Alternative Palindrome Numbers between the {a} and {b} is ",end='')
                print(i,end='')
    if ac==0:
        print("No Palindrome Values")
    else:
        print(f" = {s}.")

'''Alternative Armstrong Numbers between Given Values'''
a=abs(int(input()))
b=abs(int(input()))
if a>b:
    a,b=b,a
if a==0 or b==0:
    print("Invalid Inputs")
else:
    ac=cc=0
    for i in range(a+1,b):
        s=c=0
        t=i
        while t!=0:
            c+=1
            t//=10
        t=i
        while t!=0:
            r=t%10
            s+=r**c
            t//=10
        if s==i:
            ac+=1
            if ac%2==1:
                cc+=1
                if cc>1:
                    print(end=', ')
                if cc==1:
                    print("Alternative Armstrong Numbers between the Given Values is ",end='')
                print(i,end='')
    if ac==0:
        print("No Armstrong Numbers Between Given Values.")
    else:
        print(".")

'''Armstrong Numbers between the Given Values'''
a=abs(int(input()))
b=abs(int(input()))
if a>b:
    a,b=b,a
if a==0 or b==0:
    print("Invalid Inputs")
else:
    cc=0
    for i in range(a+1,b):
        t=i
        c=s=0
        while t!=0:
            c+=1
            t//=10
        t=i
        while t!=0:
            r=t%10
            s+=r**c
            t//=10
        if s==i:
            cc+=1
            if cc>1:
                print(end=', ')
            if cc==1:
                print("Armstrong Numbers between the Given Values is ",end='')
            print(i,end='')
    if cc==0:
        print("No Armstrong Numbers Between Given Values")
    else:
        print(".")

'''Sum of the Armstrong Numbers In The Given Range'''
a=abs(int(input()))
b=abs(int(input()))
if a>b:
    a,b=b,a
if a==0 or b==0:
    print("Invalid Inputs")
else:
    ss=cc=0
    for i in range(a,b+1):
        t=i
        s=c=0
        while t!=0:
            c+=1
            t//=10
        t=i
        while t!=0:
            r=t%10
            s+=r**c
            t//=10
        if s==i:
            cc+=1
            ss+=i
            if cc==1:
                print("Armstrong Numbers in the Given Range is ",end='')
            if cc>1:
                print(end=' + ')
            print(i,end='')
    if cc==0:
        print("No Armstrong Numbers in a Given Range.")
    else:
        print(f' = {ss}.')

'''Leap year'''
a=int(input())
if a>0:
    if a%4==0 and a%100!=0 or a%400==0:
        print("Leap Year.")
    else:
        print("Not a Leap Year.")
else:
    print("Given Year is Invalid Input.")

'''Average of Fibonacci Series in The Given Range'''
p=int(input())
q=int(input())
s=cc=0
if p>=0 and q>=0:
    a,b=0,1
    if p>q:
          p,q=q,p
    while (a<=q):
        if a>=p:
            s+=a
            cc+=1
        c=a+b
        a=b
        b=c
    if cc==0:
        print("No Fibonacci Series Values")
    else:
        print(f'{s/cc:.2f}')
else:
    print("Invalid Inputs")

'''Fibonacci Series'''
n=int(input())
cc=0
if n==0:
    print("Invalid Input")
else:
    if n<0:
        n=abs(n)
    a,b=0,1
    while True:
        cc+=1
        if cc>1:
            print(end=' ')
        print(a,end='')
        c=a+b
        a=b
        b=c
        if cc==n:
            break

'''Sum of Factorials upto N Numbers'''
a=int(input())
if a>=0:
    c=0
    s=0
    cc=1
    if a>=0:
        for i in range(1,a+1):
            cc=cc*i
            s+=cc
            c+=1
            if c==1:
                print("1+",end='')
            if c>1:
                print(end='+')
            print(cc,end='')
        if a==0:
            print(f'1={s+1}')
        else:
             print(f'={s+1}')
else:
    print("INvalid INput")

'''Fibonacci Series in the Given Range'''
n=int(input())
n1=int(input())
cc=0
if n>=0 and n1>=0:
    a,b=0,1
    if n>n1:
        n,n1=n1,n
    while a<=n1:
        if a>=n:
            cc+=1
            print(a,end=' ')
        c=a+b
        a=b
        b=c
    if cc==0:
        print("No Fibonacci Series Values")
else:
    print("Invalid Inputs")

'''Average of Alternative Fibonacci Series in Given Range'''
n=int(input())
n1=int(input())
s=cc=ac=0
if n>=0 and n1>=0:
    if n>n1:
        n,n1=n1,n
    a,b=0,1
    while a<=n1:
        if a>=n:
            cc+=1
            if cc%2==1:
                s+=a
                ac+=1
        c=a+b
        a=b
        b=c
    if cc==0:
        print("No Fibonacci Series Values")
    else:
        print(f'{s/ac:.2f}')
else:
    print("Invalid Inputs")

'''Sum of the Fibonacci Series'''
n=int(input())
s=cc=0
if n>0:
    a,b=0,1
    for i in range(1,n+1):
        s+=a
        cc+=1
        c=a+b
        a=b
        b=c
        if cc==n:
            break
    print(s)
else:
    print("Invalid Input")