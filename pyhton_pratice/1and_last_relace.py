str=input("enetr a string :")
x=input("Enter the character to be replaced: ")
r=input("Enter the character to replace with: ")
count=0
str1=str.replace(x,r,1)
str2=str1[::-1]
str3=str2.replace(x,r,1)
str4=str3[::-1]
print(str4)

