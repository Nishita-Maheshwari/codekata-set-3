def prime(n):
    for i in range(2,n):
        if(n%i)==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
num = int(input())
if(num>0):
    prime(num)
else:
    print("enter a positive number ")