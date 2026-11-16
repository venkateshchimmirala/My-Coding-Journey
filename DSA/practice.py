l=[9,5,2,6,4,3,9]
ts=sum(l)
ls=0
for i in range(len(l)):
    rs=ts-ls-l[i]
    if ls==rs:
        print(i)
        break
    ls+=l[i]
else:
    print(-1)

l=[9,5,2,6,4,3,9]
n=len(l)
p=[0]*(n+1)
for i in range(n):
    p[i+1]=p[i]+l[i]
print(p)



l=[9,5,2,6,4,3,9]
ts=sum(l)
le=0 # 16
for i in range(len(l)): #1
    if ts-le-l[i]==le:
        print(l[i])
        break
    le+=l[i]

'''min sum of sub array'''
l=[9,3,-2,15,-20,-15,50]
cs=0
min=float('inf')
for i in l:
    cs+=i
    if cs>0:
        cs=0
    if cs<min:
        min=cs
print(min)


'''wap to print all circular sub arrays of a given array'''
l=[0,1,2,3,4]
for i in range(0,len(l)):
    for j in range(len(l)):
        sub=[]
        for k in range(0,j+1):
            sub.append(l[(k+i)%len(l)])
        print(*sub)

'''wap to find max sum of circular sub array'''
l=[0,1,2,3,4]

h=[1,8,6,2,5,4,8,3,7]
max=float('-inf')
for i in range(len(h)-1):
    for j in range(i+1,len(h)):
        height=min(h[i],h[j])
        w=j-i
        area=height*w
    if area>max:
        max=area
print(max)

'''trapping rain water'''
height=[0,1,0,2,1,0,1,3,2,1,2,1]


'''Lower bond'''
l=[10,15,15,15,25,25,35,36,40,40,45]
target=15
lb=len(l)
start = 0
end= len(l)-1
while start <= end:
    mid=(start+end)//2
    if l[mid] >= target:
        lb=mid
        end=mid-1
    else:
        start=mid+1
print(lb)


#704
#34

'''Upper bond'''
l=[10,15,15,15,25,25,35,36,40,40,45]
target=15
ub=len(l)
start = 0
end= len(l)-1
while start <= end:
    mid=(start+end)//2
    if l[mid] > target:
        lb=mid
        end=mid-1
    else:
        start=mid+1
print(ub)