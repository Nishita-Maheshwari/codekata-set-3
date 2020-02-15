# Reverse words in a given string
# example
#input:
#1
#i.love.this.program
#Output :program.this.love.i





t =int(input())
while(t!=0):
    string=input()
    list_string=string.split(".")
    list_string.reverse()
    print(".".join(list_string))
    t-=1
