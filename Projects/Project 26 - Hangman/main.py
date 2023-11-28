import random

hangman_stages = ['''
  +---+
  |   |
  |   O
  |  /|\  
  |  / \ 
  |    
==========
''', '''
  +---+
  |   |
  |   O
  |  /|\  
  |  / 
  |    
==========
''', '''
  +---+
  |   |
  |   O
  |  /|\  
  |  
  |    
==========
''', '''
  +---+
  |   |
  |   O
  |  /| 
  |  
  |    
==========''', '''
  +---+
  |   |
  |   O
  |   |
  |  
  |    
==========
''', '''
  +---+
  |   |
  |   O
  |   
  |  
  |    
==========
''', '''
  +---+
  |   |
  |   
  |   
  |  
  |    
==========
''']

word_list = ["UDEMY", "APPMILLERS", "PYTHON"]

secret_word = random.choice(word_list)

blanks = []

for _ in range(len(secret_word)):
    blanks.append('_')                                


guessed_letters = []
end_game = False
lives = 6

while not end_game:
    print(" ".join(blanks))

    guess = input("Guess letter : ").upper()        # Take a single letter input from user

    if guess in guessed_letters:
        print("Letter already guessed")             # Check if already guessed or not
        continue
    else:
        guessed_letters.append(guess)

    for position in range(len(secret_word)):        # If letter present in word, replace the blanks with the word
        letter = secret_word[position]

        if guess == letter:
            blanks[position]=guess

    print(" ".join(blanks))
    print(hangman_stages[lives])

    if guess not in secret_word:                    # Decrese life by 1 if not found the letter in the secrect_word
        lives -= 1


    if lives == 0:                                  # If all lives finished, end the game
        print("You Lose !")
        end_game = True


    if "_" not in blanks:                           # Stop taking input letters when all characters are guessed
        print("You Win !")
        end_game = True

    if end_game:
        ask = input("Want to play again ? (Y/N)")
        if ask == "Y":
            secrect_word = random.choice(word_list)
            blanks = []

            for _ in range(len(secret_word)):
                blanks.append('_')
                
            guessed_letters.clear()
            end_game = False
            lives = 6
        else:
            print("See you next time !")
