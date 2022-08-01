from ast import Not
import random


choices = ["stone","paper","scissors"]
cpuScore = 0
userScore = 0

while True:
    user = input("Stone,paper,scissors: ")
    computer = random.choice(choices)
    print("User : {}, CPU : {}".format(user, computer))

    print("user value is",user)
    print("computer is",computer)
    if(user==computer):
        print("Match is Tie")
    elif(user=="stone" and computer=="paper"):
        print("Computer win")
        cpuScore+=1;
    elif(user=="paper" and computer=="scissors"):
        print("Computer win")
        cpuScore+=1;
    elif(user=="scissors" and computer=="stone"):
        print("Computer win")
        cpuScore+=1;
    elif(user=="stone" and computer=="scissors"):
        print("User win")
        userScore+=1;
    elif(user=="paper" and computer=="stone"):
        print("User win")
        userScore+=1;
    elif(user=="scissors" and computer=="paper"):
        print("User win")
        userScore+=1;
    
    print("CPU Score : {}, User Score : {}".format(cpuScore, userScore))

 

    



  