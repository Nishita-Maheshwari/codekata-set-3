n =int(input("enter the year"))
if(n%4==0):
    if(n%100==0):
        if(n%400==0):
            print("The year {} is a leap year".format(n))
        else:
            print("the year {} is not leap year".format(n))
    else:
        print("the year {} is a leap year".format(n))
else:
    print("The year {} is not a leap year".format(n))