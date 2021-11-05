secret_word = 'vipul'
guess = ""
guess_count = 0
guess_limit = 3
guess_chances = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        print(f"you have {guess_chances} chance left")
        guess_chances -= 1
        guess = input("guess word: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of chances you lose")
else:
    print("you win")