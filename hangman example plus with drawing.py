import random, hangman_draw
#original list of words
words = ["giraffe", "desk", "orange", "tree", "class"]
#initialization
total_lives = 6
rem_lives = 6
guessed_letters = ""

#choose one word
def select_word(words_list):
    return random.choice(words_list)

#print hangman stage
def print_hangman(tot_attempts, rem_attempts):
    print(hangman_draw.stages[tot_attempts - rem_attempts])

def print_selected(guessed, word):
    for c in word:
      if c in guessed:
        print(c + " ", end='')
      else:
        print("_ ", end='')

def unique_char(word):
    return "".join(set(word))

def check_guess(guess, word):
    if len(guess) == 1 and guess.isalpha():
      if guess in word:
        return True
      else:
        return False
    print("Your input was invalid!")
    return False


#Start of game
print("Welcome to HangMan! Can you guess this word?")
#Choosing a word
word = select_word(words)
print_selected(guessed_letters, word)
#printing hangman stage
print_hangman(total_lives, rem_lives)
unique_word = unique_char(word)

while (rem_lives > 0 and (len(guessed_letters) < len(unique_word))):
  guess = input("Guess a letter: ")

  if (check_guess(guess, word)):
    if guess in guessed_letters:
      print("You already guessed it.")
    else:
      guessed_letters = guessed_letters + guess
    print("Good! You guessed it right!")
  else:
    rem_lives -= 1
    print("Sorry! You guessed it wrong.")
    print(f"You lost a life. Remaining lives = {rem_lives}")

  #Print updated word
  print_selected(guessed_letters, word)
  #Print hangman stage
  if rem_lives == 0:
    print_hangman(total_lives, rem_lives+1)
  else:
    print_hangman(total_lives, rem_lives)

#Win or Lose
if rem_lives == 0:
  print("Sorry! You lost.")
else:
  print("Congratulations! You won.")
