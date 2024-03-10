#list 
marks=[55,23,87,98,45]
print(marks)
print(type(marks))
print(marks[0])
name=["krishna","karan","yash "]
print(name)
name[1]="kunal"
print(name)
#list methord 
list=[3,6,4,7,9]
#1) append 
list.append(5)
print(list)
name.append("rajesh")
print(name)
print(list.append(8))#it will return none value 
#2) short (in accending order )
list.sort()
print(list)
name.sort()
print(name)
#3) short (in decending order )
list.sort(reverse=True )
print(list)
#4) reverse 
list=[3,6,4,7,9]
list.reverse()
print(list)
#5)insert 
list=[3,6,4,7,9]
list.insert(2,12)#2 is index value of list and 12 is value instered 
print(list)
#6) remove first occurence in list 
list=[3,6,4,7,9]
list.remove(4)
print(list)
#7) pop (it revmove the value at index )
list=[3,12,6,4,7,9]
list.pop(4)#4 is index value 
print(list)
