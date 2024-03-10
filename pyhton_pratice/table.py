#print n number table usin while loop 
n=int(input("enter a number "))
i=1
table=0
print("-----------------------------------------------------------------")
while i<=10:
    table=i*n
    print(i,"\t",table)
    i+=1
print("----------------------------------------------------------------")    
a=10
b=20
a,b=b,a
print(a,b)