import random

def game(comp,you):
    if comp == you:
        return None

    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
   
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
   
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
        



print("Comp turn: Rock(r), Paper(p), Scissor(s)? ")
rand = random.randint(1,3)

if rand == 1:
    comp = 'r'
elif rand == 2:
    comp = 'p'
elif rand == 3:
    comp = 's'



you = input("Your turn: Rock(r), Paper(p), Scissor(s)? ")
a = game(comp,you)


print(f"Comp chose --> {comp} ")
print(f"You chose -->  {you} ")


if a == None:
    print("***Its a tie***")
elif a:
    print("***You won***")
else:
    print("***You lose***")
