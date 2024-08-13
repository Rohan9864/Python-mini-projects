secret=7
guess=""
limit=5
i=0
while secret!=guess: 
    if i==limit:
        print("You exceded the limit")
        print("You Lost")
        print("Try again later")
        break
    guess=int(input("Guess the number:"))
    i+=1

else:
    print("You guessed it right") 
