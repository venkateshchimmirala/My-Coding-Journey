a=int(input())
if a%2==0:
    print("Even")
else:
    print("Odd")

'''Even Numbers In The Given Range'''
a=int(input())
b=int(input())
if a>b:
    print("Invalid Range")
else:
    for i in range(a,b+1):
        if i%2==0:
            print(i,end=' ')

'''print 11 divisiors in Given Range'''
a=int(input())
b=int(input())
if a>b:
    print("Invalid Range")
else:
    c=0
    for i in range(a,b+1):
        if i%11==0:
            c+=1
            print(i,end=' ')
if c==0:
    print("No Numbers")

'''Big Of Three Numbers'''
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(f'{a} is The Biggest Number')
elif b>a and b>c:
    print(f'{b} is The Biggest Number')
else:
    print(f'{c} is The Biggest Number')

'''Case Study'''
a=int(input())
if a<0 or a>100:
    print("INVALID INPUT")
elif 91<=a<=100:
    print("SUPER SMART")
elif 81<=a<=90:
    print("SMART")
elif 71<=a<=80:
    print("SMART ENOUGH")
elif 61<=a<=70:
    print("JUST SMART")
elif 36<=a<=60:
    print("NO SMART")
else:
    print("DUMB")

'''Perform Addition, Subtraction, Multiplication and Division of 2 Numbers'''
a=int(input())
b=int(input())
p=input()
if p=="+":
    print(a+b)
elif p=="-":
    print(a-b)
elif p=="*":
    print(a*b)
elif p=="//":
    print(a//b)
elif p=="%":
    print(a%b)

'''Average of all even numbers in the given range.'''
a=int(input())
b=int(input())
if a>b:
    print("INVALID RANGE")
else:
    s=c=0
    for i in range(a,b+1):
        if i%2==0:
            c+=1
            s+=i
    print(f'{s/c:.1f}')

'''Odd Numbers in Range'''
a=int(input())
b=int(input())
if a>b:
    print("INVALID RANGE")
else:
    for i in range(a,b+1):
        if i%2==1:
            print(i,end=' ')

'''Print the Alternative Even Numbers Between the Given Numbers'''
a=int(input())
b=int(input())
ac=0
if a>0 and b>0:
    for i in range(a+1,b):
        if i%2==0:
            ac+=1
            if ac%2==1:
                print(i,end=' ')
else:
    print("Invalid Inputs")

''' program to print all alternative even numbers in the given range if no numbers then 
print NO NUMBERS if starting range is greater than ending range print INVALID INPUTS'''
a=int(input())
b=int(input())
ac=0
if a>b:
    print("INVALID INPUTS")
else:
    for i in range(a,b+1):
        if i%2==0:
            ac+=1
            if ac%2==1:
                print(i,end=' ')
    if ac==0:
        print("NO NUMBERS")

''' print sum of all even numbers in between the Given Numbers if no even numbers 
print NO NUMBERS if starting range is greater than ending range then print INVALID RANGE'''
a=int(input())
b=int(input())
s=c=0
if a>b:
    print("INVALID RANGE")
else:
    for i in range(a+1,b):
        if i%2==0:
            s+=i
            c+=1
    if c==0:
        print("NO NUMBERS")
    else:
        print(s)