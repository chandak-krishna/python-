
f = open("abc.txt",'r')
print(f.read(5))
#reading line by line 
print(f.readline())
print(f.readline())
for i in range(0,5):
    print(f.readline())
f.close()
x=open("myfile.txt","w+")
x.write("python is a good language")
print(x.read())

x.close()







