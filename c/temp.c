#include<stdio.h>
#include<conio.h>
int main(){
    int temp;
    printf("enter the temperature");
    scanf("%d",&temp);
    if (temp<0)
    {
        printf("freezing");

    }else if (temp>=0 && temp<10)
    {
        printf("cold");
    }else if (temp>=10 && temp<20)
    {
        printf("normal");
    }else if (temp>=20 && temp<30)
    {
        printf("hot");
    }else if (temp>=30 && temp<40)
    {
        printf("very hot");
    }else if (temp>=40)
    {
        printf("extremely very hot ");
    }
    return 0;
}    
    
    
    
         
