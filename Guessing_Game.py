n= 18
number_of_guesses= 1
print("You will only got 5 guesses")
while(number_of_guesses<=5):
    guess_number= int(input("Guess the number: "))
    if guess_number<18:
        print("Your guess is too low")
    elif guess_number>18:
        print("Your guess is too high")
    else:
        print("You Won!")
        print(number_of_guesses, "number of guesses taken")
        break
    print(5-number_of_guesses,"number of guesses left")
    number_of_guesses= number_of_guesses+1
if(number_of_guesses>5):
    print("Game Over")
