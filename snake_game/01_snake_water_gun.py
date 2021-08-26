import random

def game(comp,b):
    if(comp== b):
        return None
    elif (comp=='s'):
        if b=='w':
            return False
        elif b=='g' :
            return True    
    elif (comp=='w'):
        if b=='g':
            return False
        elif b=='s' :
            return True    
    elif (comp=='g'):
        if b=='s':
            return False
        elif b=='w' :
            return True                    

print("computer's turn : snake(1) water(2) Gun(3) ")
rand_no=random.randint(1,3)
if (rand_no==1):
    comp='s'
elif (rand_no==2):
    comp='w'
elif (rand_no==3) :
    comp='g'        
b=input("player's turn : snake(1) water(2) Gun(3) ")
a=game(comp,b)
print(f"computer choose {comp}")
print(f"you choose {b}")
if a== None:
    print("Game is Tie ")
elif a==True:
    print("You win") 
else :
    print("you loss ")       