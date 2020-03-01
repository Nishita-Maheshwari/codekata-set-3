#0,0,7,6,14,12,21,18,28......
# Find the 15th term of series
#explation:  7 {0,7,14,21,28,35....}
             #6 {0,6,12,18,24,30.....}

n =int(input("enter the numbers :"))
a=0
b=0
for i in range(1,n+1):
    if(i%2!=0):
        a=a+7
    else:
        b=b+6
if(n%2!=0):
    print('{} term of series is {}'.format(n,a-7))
else:
    print('{} term of series is {}'.format(n,b-6))
