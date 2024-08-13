a="welcome"
print(a.center(70,"-"))
print("A Rock Paper Scissor Game")
print("!!!Rule R>S S>P, P>R!!!")

import random
computer=random.choice(["R","P","S"])

user=input("Enter your Choice:\n 'R' for Rock \n 'S' for Scissor \n  'P' for Paper :")
user=user.upper()

print(f"Your choice is :{user}")
print(f"Computer choice is {computer}")

if (user=="R" and computer=="S") or (user=="P" and computer=="R") or (user=="S" and computer=="P") :
    print("!!! Congrats, You Won!!!")
elif user==computer:
    print("!!!IT is a Draw!!!")
elif user not in ["R","P","S"] :
    print("!!! Invalid Input !!!")
else:
    print("!!!Alas,You Lose!!!")

