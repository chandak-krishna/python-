#condtional statement 
#1)if 
age=20
if(age>=18):
    print("you cane vote")# python does not work on {}it worrk n indentition 

#2)if-elif-else
light="green"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
    print("drive carefully")
else:
    print("error")                

print("code is completed ")  
#3)nesting 
age=77
if(age>=18):
    if(age>=80):
        print("cannot drive ")
    else:
        print("drive")
else:
    print("cannot drive")
