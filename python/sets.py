#set
sets={1,2,3,4,5,"hellow", "world",2,4, "hellow"}#it will ignore the dupicate value
print(sets)
print(type(sets))
print(len(sets))#it will also  ignore dupicate value dupicate 
# set methord 
collection={2,4,5,"xyz"}
#1) add 
collection.add(78)
collection.add("abc")
print(collection)
#2) remove
collection.remove(2)
collection.remove("xyz")
print(collection)
#3) pop(remove a random varibe)
collection.pop()
print(collection)
#4) clear
collection.clear()
print(collection)
#5) union 
collection={2,4,5,"xyz","hellow"}
xyz=collection.union(sets)
print(xyz)
#6) intersection 
abc=collection.intersection(sets)
print(abc)
