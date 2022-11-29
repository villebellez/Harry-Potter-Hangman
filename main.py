import random
import hangman_art as art
import hangman_words as words

#Computer generated word choice.
chosen_word = random.choice(words.word_list) 
word_length = len(chosen_word)

#Game Elements.
the_end = False
lives = 6

#Logo and welcome message.
print(art.logo)
print("\nTry to guess the magical word!\n")

#TESTING ONLY: Chosen Word.
# print(f'The word is: {chosen_word}.')

#Declaring original amount of blank spaces.
display = []
for letter in chosen_word:
  display.append("_")
print(f"{' '.join(display)}")

#Prompt user to guess a letter until there are no more blanks.
while the_end == False:
  guess = input("\nGuess a letter:\n").lower()
  if guess in display:
    print("\nYou have already guessed that letter. Try again.")
  for char in range(word_length):
    letter = chosen_word[char]
    if letter == guess:
      display[char] = letter 
      
#If wrong, lose a life.
  if guess not in chosen_word:
    lives -= 1
    print(f"\nYour guess is not in the word. You lose a life.")
    
#What ASCII art to display during an active game.  
  print(art.stages[lives])
  
#Show user their progress. 
  print(f"{' '.join(display)}")
  
#TESTING ONLY: Lives left.  
  # print(f'\nLIVES LEFT: {lives}')

#Winning Message.
  if "_" not in display:
        the_end = True
        print("\nYou've Won!")

#Losing Message.
  if lives == 0:
        the_end = True
        print(art.stages[0])
        print(f"You\'ve lost! The word was: {chosen_word}.")