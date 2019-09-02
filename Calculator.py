def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multipy(x,y):
    return x*y
def divide(x,y):
    return x/y
print("select option")
print("1.add")
print("2.subtract")
print("3.multipy")
print("4.divide")
choice =int(input("enter choice(1/2/3/4)"))
n1 =int(input(" "))
n2=int(input(" "))
if(choice==1):
    print(n1,"+",n2,"=",add(n1,n2))
elif(choice==2):
    print(n1,"-",n2,"=",subtract(n1,n2))
elif(choice==3):
    print(n1,"*",n2,"=",multipy(n1,n2))
elif(choice==4):
    print(n1,"/",n2,"=",divide(n1,n2))
else:
    print("invalid choice")
