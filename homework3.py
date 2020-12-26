#homework 3
import random
liste=["python","pencil","eraser","delphi"]
b=list(random.choice(liste))
c=["","","",""]
liste1=("","")
d=len(b)
name=input("Please entering your name:")
print(f"---Welcome to the Hangman game {name}---")
def hangman(word):
    if(d==6):
        c.extend(liste1)
    heart=4
    while True:
        a = str(input("Please entering a letter: "))
        if a=="exit":
            print("You're exit the game")
            break
        else:
            if a.isalpha()==True:
                a=a.lower()
                if(a in b):
                    e = b.index(a)
                    c.insert(e,a)
                    c.pop(e+1)
                    print(c)
                    print("Do you want to guess(yes)")
                elif (a=="yes"):
                    g=str(input("Please enter your answer: "))
                    if(list(g)==list(b)):
                        print("Congratulations")
                        break
                    else:
                        heart-=1
                        print(f"You have {heart} heart stay")
                        print("Wrong")
                else:
                    heart-=1
                    print(f"You have {heart} heart stay")
                    print(f"Wrong letter is {a}")
                if(heart==0):
                    print("The man hanged!!")
                    break
            else:
                print("Please just enter letters!!")
                continue
    return a
hangman(liste)
