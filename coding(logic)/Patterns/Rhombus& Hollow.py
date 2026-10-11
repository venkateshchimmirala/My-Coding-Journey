''' *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * * 
    *
    '''
n=int(input())
if n>0:
    for i in range(1,n+1):
        print(" "*(n-i),end='')
        for j in range(1,i+1):
            print("*",end=' ')
        print()
    for i in range(n-1,0,-1):
        print(" "*(n-i),end='')
        for j in range(1,i+1):
            print("*",end=' ')
        print()
else:
    print("Invalid Input")

'''
1
2 4
3 6 9
4 8 12 16
5 10 15
6 12
7'''
n=int(input())
if n>0:
    for i in range(1,n+1):
        c=i
        for j in range(1,i+1):
            print(c,end=' ')
            c+=i
        print()
    for i in range(n-1,0,-1):
        c=n+1
        for j in range(1,i+1):
            print(c,end=' ')
            c+=n+1
        print()
        n+=1
else:
    print("Invalid Input.")

'''
1 2 3 4 5 4 3 2 1
  2 3 4 5 4 3 2
    3 4 5 4 3
      4 5 4
        5
      4 5 4
    3 4 5 4 3
  2 3 4 5 4 3 2
1 2 3 4 5 4 3 2 1'''
n=int(input())
if n>0:
    for i in range(1,n+1):
        print("  "*(i-1),end='')
        for j in range(i,n+1):
            print(j,end=' ')
        for j in range(n-1,i-1,-1):
            print(j,end=' ')
        print()
    for i in range(n-1,0,-1):
        print("  "*(i-1),end='')
        for j in range(i,n+1):
            print(j,end=' ')
        for j in range(n-1,i-1,-1):
            print(j,end=' ')
        print()
else:
    print("Invalid Input")

'''
01 02 03 04
05       06
07       08
09 10 11 12'''
n=int(input())
if n>0:
    c=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n or j==1 or j==n:
                print(f'{c:02}',end=' ')
                c+=1
            else:
                print("  ",end=' ')
        print()
else:
    print("Invalid Input")

'''
*
* *
*  * 
*   *
*    *
*   *
*  *
* *
*'''
n=int(input())
if n>0:
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j==1 or i==j:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            if j==1 or i==j:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
else:
    print("Invalid Input")

''' * *
    * *
* * * * * *
* * * * * * 
    * * 
    * * '''
n=int(input())
if n>0:
    if n%2==1:
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (n//2)+1==i or (n//2)+1==j:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
    else:
        for i in range(1,n+1):
            for j in range(1,n+1):
                if n//2==i or (n//2)+1==i or n//2==j or (n//2)+1==j:
                    print("*",end=' ')
                else:
                    print(" ",end=' ')
            print()
else:
    print("Invalid Input")

'''      *
        * *
       * * * 
      * * * * 
     * * * * * 
    *         *
   * *       * * 
  * * *     * * * 
 * * * *   * * * *
* * * * * * * * * * '''
n=int(input())
if n>0:
    for i in range(1,n+1):
        print(" "*((n-i)+n),end='')
        for j in range(1,i+1):
            print("*",end=' ')
        print()
    for i in range(1,n+1):
        print(" "*(n-i),end='')
        for j in range(1,i+1):
            print("*",end=' ')
        print("  "*(n-i),end='')
        for j in range(1,i+1):
            print("*",end=' ')
        print()
else:
    print("Invalid Input")

''' *         *
   * *       * *
  * * *     * * *
 * * * *   * * * * 
* * * * * * * * * * 
 * * * *   * * * *
  * * *     * * * 
   * *       * *
    *         *
    '''
n=int(input())
if n>0:
    for i in range(1,n+1):
        print(' '*(n-i),end='')
        for j in range(1,i+1):
            print("*",end=' ')
        print("  "*(n-i),end='')
        for  j in range(1,i+1):
            print("*",end=' ')
        print()
    for i in range(n-1,0,-1):
        print(" "*(n-i),end='')
        for j in range(1,i+1):
            print("*",end=' ')
        print("  "*(n-i),end='')
        for j in range(1,i+1):
            print("*",end=' ')
        print()
else:
    print("Invalid Input")
