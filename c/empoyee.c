#include <stdio.h>
 

struct employee{
    char    name[50];
    int     empId;
    float   salary;
};
 
int main()
{
    
    struct employee emp[12];
    int n=5,i;

     for(i=0;i<n;i++){
    
    printf("\nEnter details :\n");
    printf("Name ?:");          
    scanf("%s",emp[i].name);
    printf("ID ?:");            
    scanf("%d",&emp[i].empId);
    printf("Salary ?:");        
    scanf("%f",&emp[i].salary);
     }
     for(i=0;i<n;i++)
     {
    
    printf("\nEntered detail is---------\n :");
    printf("Name: %s\n"   ,emp[i].name);
    printf("Id: %d\n"     ,emp[i].empId);
    printf("Salary: %f\n",emp[i].salary);
     }

     for(i=0;i<n;i++){
        if (emp[0].name=='a'&&emp[0].name=='A')
        {
        printf("%s\n",emp[i].name);
        }
        
     }
    return 0;
}