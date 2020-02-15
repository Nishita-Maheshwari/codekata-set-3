# Reverse words in a given string
# example
#input:
#1
#i.love.this.program
#Output :program.this.love.i

t =int(input())
while(t!=0):
    s=input()
    ls=s.split(".")
    ls.reverse()
    print(".".join(ls))
    t-=1
