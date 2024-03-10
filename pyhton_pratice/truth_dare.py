#i am  making a truth and dare game 
import random
#truth question 
print("------------------welecome to the game Truth and Dare -----------------------------\n")
T_Q=("Have you ever lied to your parents","What's your biggest fear?",
"What's the most embarrassing thing that's ever happened to you?",
"What is the weirdest thing you have ever eaten",
"What is the wildest thing you have ever done?","What's the craziest thing you've ever done?")
#dare question 
D_Q=("Do 10 sit-ups, 10 push-ups, and 10 squats","Sing the alphabet backward",
"Eat a piece of raw garlic","Eat a snack without using you hands",
"Make a prank call with your friend","Sing instead of speaking for the next round")
point=0
z=0

while z<5:
    x=input("\t\t\ttruth or dare\n ")
    #if truth
    if(x=="truth" or x=="TRUTH" ): 
    
        random.seed()
        i=random.randint(0,5)
        print(T_Q[i])
        ans_t=input("enetr your answer ") 
        point=point+1
    # if dare 
    elif(x=="dare" or x=="DARE"):
    
        random.seed()
        y=random.randint(0,5)
        print(D_Q[y])
        ans_d=input("enetr your answer / task done ")
        point=point+1

    else:
        print("please type correctly")
    z=z+1

print("\n\t\t   Total point are ",point,"\n")
print("-------------------------end of game----------------------")