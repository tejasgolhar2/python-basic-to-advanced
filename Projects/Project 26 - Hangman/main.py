import random


word_list = ["UDEMY", "APPMILLERS", "PYTHON"]
secret_word = random.choice(word_list)
guessed_letters = []

for i in range(len(secret_word)):
    guessed_letters.append('_')
print(guessed_letters)

while True:
    if '_' not in guessed_letters:
        print("You Win")
        break
    g_letter = input("Guess a letter : ").upper()

    c = secret_word.count(g_letter)

    if g_letter in guessed_letters:
        if guessed_letters.count(g_letter)<c:
            
        else:
            print("Letter Already Guessed")
    else:
        if g_letter in secret_word:
        
            

            guessed_letters[secret_word.index(g_letter)]=g_letter
            print(guessed_letters)
        else:
            print("Draw a part")