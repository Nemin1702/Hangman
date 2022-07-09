import random

name=(input("What is your name: "))
print("Good luck", name,"!g")
wordlist=['assess','onomatepea','inverted','cautious','idealistic','anaphora','pragmatism','pheonix','table','delusional','juxtaposition','laboratory','wiring','fourteen','rhythm']
word=random.choice(wordlist)
print("Guess a letter of the word! ")
guess=("")
turns=12
while turns>0:
        failed=0
        for char in word:
            if char in guess:
                print(char,end=" ")
            else:
                print("_",end=" ")
                failed+=1
        if failed == 0:
            print("You win ,Congrats!")

            print("The word is ", word)
            break
        guess1=input("\n Guess a letter from the word: ")
        guess+=guess1
        if guess1 not in word:
            turns-=1
            print("Wrong move! Your have ", turns, "turns left")
            if turns==0:
                print("Your ran out of turns! Better luck next time!")