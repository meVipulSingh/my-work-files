secret_number = "VIPUL".lower()
guess = ""
number_of_guess = 0
chance_of_guess = 3
out_of_guesses = False
chances_left = 3

while guess != secret_number and not (out_of_guesses):
    if number_of_guess < chance_of_guess:
        print(f"you have {chances_left} chance left ")
        chances_left -= 1
        guess =(input("Enter your guess: "))
        number_of_guess += 1
    else:
        out_of_guesses = True
    
if out_of_guesses:
    print("you lose")
else:
    print("you win")
    




