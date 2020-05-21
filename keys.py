#NOTE: Time is 30 minutes to solve this problem using any of these programming languages c, c+ +, java, Perl, python 2.7
#Problem statement 
#One programming language has the following keywords that cannot be used as identifiers:
#break, case, continue, default, defer else, for, func, goto, if, map, range, return, Struct, type, var
#Write a program to find if the given word is keyword or not
#Example-1
#Input: defer
#Expected Output: defer is a keyword
#Example-2
#Input: While
#Expected Output: while is not a keyword
#PROGRAM IN python :

keywords = ["break" ,"case" ,"continue","default","defer", "else" ,
     "for","func", "goto", "if" , "map", "range", "return",  "struct" ,  
     "type" , "var"]

data = input()
present = False

for i in keywords:
    if (i == data):
        present = True
        
if(present):      
    print(data," is present")
else:
    print(data," is not present")
