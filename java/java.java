import java.util.Scanner;

public class java {
    public static void main(String[] args) {
        int[] marks =new int[40];
        Scanner a=new Scanner(System.in);
        
        int sum=0;
        for(int i=0;i<=5;i++){
            System.out.println("enter your "+i+"subject marks");
           marks[i]=a.nextInt();
           sum=sum+marks[i];
        }
        for(int i=0;i<=5;i++){
            System.out.println("your "+i+"subject marks is "+marks[i]);
            System.out.println(sum);
        }
        
    }
    }
    

