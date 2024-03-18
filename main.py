import random

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

from hangman_art import logo, stages
print(logo)

#Create blanks
display = []

for _ in range(word_length):
    display += "_"

print(" ".join(display) + "\n")
  
#Starting game
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Alert the user when a letter has already been guessed
    if guess in display:
      print(f"{guess} has been already guessed!\n")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
      print(f"{guess} is incorrect! You lose a life.\n")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.\n")
        answer = ""
        for i in range(word_length):
          answer += chosen_word[i]
          answer += " "
        
        print(f"The correct answer was \n{answer}")

    #Join all the elements in the list and turn it into a String.
    if lives != 0:
      print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Show the hangman
    print(stages[lives])