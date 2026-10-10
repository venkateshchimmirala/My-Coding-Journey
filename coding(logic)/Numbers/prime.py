a=int(input())
fc=0
for i in range(1,a+1):
    if a%i==0:
        fc+=1
if fc==2:
    print("Given Number Is a Prime")
else:
    print("Given Number is Not a Prime")