#tupple (immutable data type )
tup=(12,4,34,55,60)
print(type(tup))
print(tup)
print(tup[1])
# tup[1]=10 (error)
#tupple sclicing 
print(tup[1:3])
#tupple methord 
tupp=(1,4,64,33,90,33,2,45,22,33)
#1)index(it will print the index of the value )
print(tupp.index(64))#64 is present in tupple and index is 2
#2) count (it find the occrence of the element in tupple )
print(tupp.count(33))


