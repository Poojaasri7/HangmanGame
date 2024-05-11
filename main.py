import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
class bcolors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(bcolors.OKGREEN + f"\n {''.join(logo)}\n\n" + bcolors.ENDC) 




display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
      print(f"\nYou've already guessed {guess}\n")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life\n")
        lives -= 1
        if lives == 0:
           end_of_game = True
           print("-----YOU LOSE!-----\n")
           print(bcolors.FAIL + "The answer was --->  " + bcolors.ENDC + bcolors.OKGREEN + f"{chosen_word}\n" + bcolors.ENDC)

    print(f"\t\t\t{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(bcolors.HEADER+ "\n\nCongratulations!\nYOU WON THE GAME :)\n" + bcolors.ENDC)

    print(bcolors.OKCYAN + stages[lives] + bcolors.ENDC)