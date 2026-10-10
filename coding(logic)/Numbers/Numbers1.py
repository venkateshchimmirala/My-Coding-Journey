a=int(input())
fc=0
for i in range(1,a+1):
    if a%i==0:
        fc+=1
if fc==2:
    print("Given Number Is a Prime")
else:
    print("Given Number is Not a Prime")


'''First N No of Prime Numbers Without Factors Count'''
a=int(input())
if a>0:
    c=0
    p=1
    while True:
        fc=0
        for i in range(1,p+1):
            if p%i==0:
                fc+=1
        if fc==2:
            c+=1
            if c>1:
                print(end=', ')
            print(p,end='')
        p+=1
        if c==a:
            break
else:
    print("Invalid Input")

'''All Factors of The Given Number'''
a=int(input())
if a>0:
    for i in range(1,a+1):
        if a%i==0:
            print(i,end=' ')
else:
    print("Invalid Input")

'''' Sum of all The Primes Numbers Between The Given Values'''
a=int(input())
b=int(input())
s=0
if a>0 and b>0:
    for i in range(a+1,b):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            s+=i
    print(s)
else:
    print("Invalid Inputs")

'''Sum of all Alternative Prime Numbers Between The Given Values'''
a=int(input())
b=int(input())
ac=s=0
if a>0 and b>0:
    for i in range(a+1,b):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            ac+=1
            if ac%2==1:
                s+=i
    if ac==0:
        print("No Prime Numbers")
    else:
        print(s)
else:
    print("Invalid Inputs")

'''Alternative Prime Numbers In the Given Range'''
a=int(input())
b=int(input())
if a>0 and b>0:
    c=ac=0
    for i in range(a,b+1):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            ac+=1
            if ac%2==1:
                c+=1
                if c>1:
                    print(end=', ')
                print(i,end='')
else:
    print("Invalid Inputs")

'''All Prime Factors of a Given Number'''
a=int(input())
c=0
if a<0:
    a=abs(a)
if a==0:
    print("Invalid Input")
else:
    for i in range(1,a+1):
        if a%i==0:
            fc=0
            for j in range(1,i+1):
                if i%j==0:
                    fc+=1
            if fc==2:
                c+=1
                print(i,end=' ')
    if c==0:
        print("No Prime Factors")

'''Prime Numbers in The Given Range'''
a=int(input())
b=int(input())
c=0
if a>0 and b>0:
    for i in range(a,b+1):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            c+=1
            if c>1:
                print(end=', ')
            print(i,end='')
else:
    print('Invalid Inputs')

'''Smallest Digit in Given Number'''
n=int(input())
if n>0:
    s=9
    while n!=0:
        r=n%10
        if r<s:
            s=r
        n=n//10
    print(f'Smallest Digit in a Given Number is {s}.')
else:
    print("Invalid Input.")

'''Sum of " N " Natural Numbers (Without Using Formula)'''
n=int(input())
s=0
c=0
if n==0:
    print("InvaLid Input.")
elif n<0:
    print("Sorry! you have Entered Negative Values.")
else:
    for i in range(1,n+1):
        s+=i
        c+=1
        if c==1:
            print(f"Sum of 'N' Natural Numbers is ",end='')
        if c>1:
            print(end=" + ")
        print(i,end='')
    print(f' = {s}.')

'''Count No Of Digits in Given Number'''
a=int(input())
t=a
t=abs(t)
c=0
if a==0:
    print("InvaliD Input")
else:
    while t!=0:
        c+=1
        t//=10
    if c==1 and a>0:
        print(f"Given Number consists of only {c} Digit.")
    elif c>1 and a>0:
        print(f"Given Number consists of {c} Digits.")
    elif c==1 and a<0:
        print(f"Given Number consists of only {c} Digit and it is Negative Value.")
    else:
        print(f" Given Number consists of {c} Digits and it is Negative Value.")

'''Perfect Square or Not'''
a=int(input())
if a==0 or a<0:
    print("InvaliD Input")
else:
    b=False
    for i in range(1,a+1):
        if i*i==a:
            b=True
            break
        if i*i>a:
            break
    if b==True:
        print("Given Number is a Perfect Square.")
    else:
        print("Given Number is Not a Perfect Square.")

'''Sum of The Odd Positions in a Given Number'''
a=int(input())
if a>0:
    c=rev=s=0
    while a!=0:
        r=a%10
        c+=1
        if c%2==1:
            s+=r
        a//=10
    print(s)
else:
    print("Invalid Input")

'''Sum of The Even Digits in a Given Number'''
a=int(input())
if a>0:
    s=0
    while a!=0:
        r=a%10
        if r%2==0:
            s+=r
        a//=10
    print(s)
else:
    print('Invalid Input')

'''Sum of Digits in Given Number'''
a=int(input())
t=a
rev=c=0
if a>0:
    while a!=0:
        r=a%10
        rev=rev*10+r
        a//=10
    while rev!=0:
        c+=1
        if c>1:
            print(end=" + ")
        d=rev%10
        print(d,end='')
        rev//=10
    print(".")
else:
    print("Invalid Input.")

'''Highest Digit in Given Number'''
a=int(input())
if a>0:
    h=1
    while a!=0:
        r=a%10
        if r>h:
            h=r
        a//=10
    print(f"Highest Digit in a Given Number is {h}.")
else:
    print("Invalid Input.")