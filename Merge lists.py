a=[]
c=[]
n1=int(input(""))
for i in range(1,n1+1):
    b=int(input(""))
    a.append(b)
n=int(input(""))
for i in range(1,n+1):
    h=int(input())
    c.append(h)
new=zip(a,c)
new=list(new)
print(new)
#print((a+c))