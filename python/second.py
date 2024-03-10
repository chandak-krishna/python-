#string 
#type to create string 
str1="krishna is my name\n . how are you \t i am fine "
str2='krishna'
str3='''krishna'''
#escape scequence \n (new line ) \t (tab)
print(str1)
#concation in string
st1="krishna"
st2="chandak"
print(st1+st2)
print(len(st1))
#spacing btw two sting 
final_st=st1+" "+st2
print(st1+" "+st2)
print(final_st)
#indexing 
name="hellow"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
#slicing
string="krishna is my name. how are you i am fine"
print(string[3:9])#ending index will not be included (in this 9 is not included )
print(string[:5])#same  as print(string[0:5])
print(string[3:len(string)])#same as print(string[3:])
#negative index sclicing 
string1="apple"
print(string1[-3:-1])
