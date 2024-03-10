#restuant bill maker 
#taking input customer name 
cutomer_name=input("Enter your name : ")
cutomer_phoneno=int(input("Enetr your phone no "))
menu=("pizza        \t200\n","burger       \t150\n","chillie paner\t250\n","noodles      \t100\n",
      "chiken       \t300\n","snadwitch\t80\n","hot dog      \t200\n","french fries\t250\n",
      "passta      \t200\n","maggi       \t100\n")
x=len(menu)
total=0
a=[]

#taking order from customer 
for i in range(0,x):
    print(menu[i])
for i in range(0,50):
    y=input("plz enter your order :\t ")
    a.append(y)
    if a[i] =='done':
        break
    elif a[i] =='burger':
        total=total+150
    elif a[i] =='chillie paner':
        total=total+250
    elif a[i] =='noodles':
        total=total+100
    elif a[i] =='chicken':
        total=total+300
    elif a[i] =='sandwitch':
        total=total+80
    elif a[i] =='hot dog':
        total=total+200
    elif a[i] =='french fries':
        total=total+250
    elif a[i] =='passta':
        total=total+200
    elif a[i] =='maggi':
        total=total+100
    elif a[i]=='pizza':
        total=total+200
from os import system, name
from time import sleep
sleep(2)
system('cls')       

#printing bill of the customer 

print("\t\t\tBILL\t\t\t")
print("--------------------------------------------------------------------------")
print("NMAME        :",cutomer_name)
print("PHONE NUMBER :",cutomer_phoneno)
print("--------------------------------------------------------------------------")
print("ORDER        \tRATE")
print("--------------------------------------------------------------------------")
b=len(a) 
for j in range(0,b-1):
    if a[j] =='burger':
        print("burger       \t150\n")
    elif a[j] =='chillie paner':
        print("chillie paner\t250\n")
    elif a[j] =='noodles':
        print("noodles      \t100\n")
    elif a[j] =='chicken':
        print("chiken       \t300\n")
    elif a[j] =='sandwitch':
        print("snadwitch    \t80\n")
    elif a[j] =='hot dog':
        print("hot dog      \t200\n")
    elif a[j] =='french fries':
        print("french fries \t250\n")
    elif a[j] =='passta':
        print("passta       \t200\n")
    elif a[j] =='maggi':
        print("maggi        \t100\n")
    elif a[j]=='pizza':
        print("pizza        \t200\n")
print("--------------------------------------------------------------------------")
print("total  \t",total)     