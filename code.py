#NUMBER GUESSING GAME
import random 
print("WELCOME TO NUMBER GUESSING GAME!") 
while True:
    print("I'M CHOOSING A NUMBER FROM 1 TO 100")
    num=random.randint(1,100)
    attempt=0
    ans="yes"
    while ans=='yes':
        try:
            attempt+=1
            guess=int(input("ENTER YOUR GUESS: ")) 
            if guess<num:
               print("TOO LOW :(")
            elif guess>num:
               print("TOO HIGH :(")
            else:
                print("YOU GOT IT! \nHAVE A COOKIE!! :)")
                print("YOU GUESSED IT IN",attempt,"ATTEMPT(S)")
                break
        except ValueError:
            print("PLEASE ENTER A VALID INPUT")
    ans=input("Do you want to continue playing?")
