num=(input("enetr a number :"))
x=num[::-1]
z=x[0:3]
z=z[::-1]
y=int(z)%3
if y==0:
    print("true")
else:
    print("false")    