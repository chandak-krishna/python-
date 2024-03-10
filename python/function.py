#function 
def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum

#function calling 
x=cal_sum(20,25)
print(x)

def aveg(a,b,c):
    avg=(a+b+c)/3
    return avg

x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
avg_sum=aveg(x,y,z)
print(avg_sum)