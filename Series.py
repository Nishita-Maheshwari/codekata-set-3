# 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187,..................
# .....multiple by 2
# .......multiply by 3

n = int(input("enter the number"))
a = 1
b = 1
for i in range(1, n + 1):
    if (i % 2 != 0):
        a = a * 2
    else:
        b = b * 3
if (n % 2 != 0):
    print("\n{} term of seies is {}\t".format(n, a // 2))
else:
    print("\n{} term of seies is {}\t".format(n, b // 3))
