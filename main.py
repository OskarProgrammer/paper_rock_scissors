
import os as system
from random import randint, choice

def who_won(user,computer):
    global user_winning
    global computer_winning
    if user==computer:
        print("DRAW")
        print(f"Wynik (user:computer)--> {user_winning}:{computer_winning}",end="\n")
    
        
    
    elif user == "paper" and computer == "rock":
        print("User is the winner!!!")
        user_winning+=1
        print(f"Wynik (user,computer) --> {user_winning}:{computer_winning}",end="\n") 
    elif user == "rock" and computer == "scissors":
        print("User is the winner!!!")
        user_winning+=1
        print(f"Wynik (user,computer) --> {user_winning}:{computer_winning}",end="\n") 

    elif user=="scissors" and computer=="paper":
        print("User is the winner!!!")
        user_winning+=1
        print(f"Wynik (user,computer) --> {user_winning}:{computer_winning}",end="\n") 

    else:
        print("Computer is the winner")
        computer_winning+=1
        print(f"Wynik (user,computer) --> {user_winning}:{computer_winning}",end="\n") 

    
        


system.system("cls")

lista=["paper","rock","scissors"]
user_winning=0
computer_winning=0
dic={
    "paper" : "rock",
    "rock"  : "scissors",
    "scissors"  : "paper"
}

positive=["yes","Yes","YES","Tak","TAK","tak"]

print("Paper, rock, scissors")
print("The rules are easy to understand \n 1.Paper is winning with rock \n 2.Rock is winning with scissors \n 3.Scissors are winning with paper")
print("The computer is chosing from the list lista his choice by module random ")
print("Then you will choose your choice")
print("After it will give the information who won and will ask if you want to continue or stop the game (your choice)")
print("Gotowy? ")
system.system("pause>nul")

while True:
    system.system("cls")
    
    computer=choice(lista)
    print (f"The computer chose",end="\n")
    print("Now your turn: ")
    user=input("")
    while user not in lista:
        system.system("cls")
        print("Nie podales prawidlowego wyboru (paper,rock,scissors):")
        print("Sprobuj ponownie ")
        user=input("")
    
    system.system("cls")

    print(f"Wybor komputera: {computer}\nTwoj wybor:{user}")

    
    who_won(user,computer)
    
    print("You want to play still? ",end="")
    decyzja=input("")
    if decyzja in positive:
        continue
    else:
        break


    


