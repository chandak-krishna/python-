#string functions 
str="i am A coder and i am learing python"

#1)endswith() 
print(str.endswith("on"))#true
print(str.endswith("er"))#false
#2)capaitalize()
print(str.capitalize())#first letter will be capatile
print(str)#not capatile  
str1=str.capitalize()
print(str1)#will pernment be capatile 
#3)replace()
print(str.replace("a","o"))
print(str.replace("python","coding language's"))
print(str.replace("k","o"))#nothing will happen 
#4)find()
print(str.find("a"))#2
print(str.find("python"))
print(str.find("k"))#-1 show it is not present in string 
#5)count()
print(str.count("am"))
print(str.count("a"))


